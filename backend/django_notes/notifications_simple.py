# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    """
    Notification model to store user notifications
    """
    USER_CHOICES = [
        ('file_manager', 'File Manager'),
        ('task_manager', 'Task Manager'),
        ('user_system', 'User System'),
        ('support', 'Support'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    application = models.CharField(max_length=50, choices=USER_CHOICES)
    redirect_url = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def is_recent(self):
        """
        Check if notification is less than 2 days old
        """
        return timezone.now() - self.timestamp <= timezone.timedelta(days=2)

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Notification

@login_required
def notification_list(request):
    """
    View to list user notifications
    """
    notifications = Notification.objects.filter(
        user=request.user, 
        timestamp__gte=timezone.now() - timezone.timedelta(days=2)
    )
    
    return render(request, 'notifications/list.html', {
        'notifications': notifications
    })

@login_required
def mark_notification_read(request, notification_id):
    """
    Mark a specific notification as read
    """
    notification = get_object_or_404(
        Notification, 
        id=notification_id, 
        user=request.user
    )
    notification.is_read = True
    notification.save()
    
    # Redirect to the associated URL if exists
    if notification.redirect_url:
        return redirect(notification.redirect_url)
    
    return redirect('notification_list')

@login_required
def delete_notification(request, notification_id):
    """
    Delete a specific notification
    """
    notification = get_object_or_404(
        Notification, 
        id=notification_id, 
        user=request.user
    )
    notification.delete()
    
    return redirect('notification_list')

@login_required
def clear_notifications(request):
    """
    Clear all user notifications
    """
    Notification.objects.filter(
        user=request.user, 
        timestamp__gte=timezone.now() - timezone.timedelta(days=2)
    ).delete()
    
    return redirect('notification_list')

# Helper function to create notifications
def create_notification(user, message, application, redirect_url=None):
    """
    Utility function to create notifications
    """
    return Notification.objects.create(
        user=user,
        message=message,
        application=application,
        redirect_url=redirect_url
    )

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/mark/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('notifications/clear/', views.clear_notifications, name='clear_notifications'),
]

# notifications/list.html (Bootstrap Template)
"""
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h3 class="card-title">Notifications 
                        <span class="badge bg-primary">{{ notifications.count }}</span>
                    </h3>
                    {% if notifications %}
                    <a href="{% url 'clear_notifications' %}" class="btn btn-danger btn-sm">
                        Clear All
                    </a>
                    {% endif %}
                </div>
                <div class="card-body">
                    {% if notifications %}
                        {% for notification in notifications %}
                        <div class="notification-item 
                            {% if not notification.is_read %}bg-light{% endif %} 
                            mb-2 p-2 rounded">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <strong>{{ notification.get_application_display }}</strong>
                                    <p>{{ notification.message }}</p>
                                    <small class="text-muted">
                                        {{ notification.timestamp|timesince }} ago
                                    </small>
                                </div>
                                <div class="notification-actions">
                                    {% if not notification.is_read %}
                                    <a href="{% url 'mark_notification_read' notification.id %}" 
                                       class="btn btn-sm btn-outline-primary me-2">
                                        Mark Read
                                    </a>
                                    {% endif %}
                                    <a href="{% url 'delete_notification' notification.id %}" 
                                       class="btn btn-sm btn-outline-danger">
                                        Delete
                                    </a>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    {% else %}
                        <p class="text-center text-muted">No notifications</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

# base.html (Include Notifications Bell in Navbar)
"""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <!-- Other navbar items -->
        <div class="navbar-nav ms-auto">
            <div class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="notificationDropdown" 
                   role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    <i class="bi bi-bell"></i>
                    {% with unread_count=user.notifications.filter(is_read=False).count %}
                        {% if unread_count %}
                        <span class="badge bg-danger">{{ unread_count }}</span>
                        {% endif %}
                    {% endwith %}
                </a>
                <ul class="dropdown-menu" aria-labelledby="notificationDropdown">
                    {% for notification in user.notifications.all|slice:":5" %}
                    <li>
                        <a class="dropdown-item" href="{% url 'mark_notification_read' notification.id %}">
                            {{ notification.message }}
                        </a>
                    </li>
                    {% empty %}
                    <li><span class="dropdown-item text-muted">No notifications</span></li>
                    {% endfor %}
                    <li><hr class="dropdown-divider"></li>
                    <li>
                        <a class="dropdown-item text-primary" href="{% url 'notification_list' %}">
                            View All Notifications
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</nav>
"""

# Example of creating a notification in another view
def upload_file(request):
    # ... file upload logic
    create_notification(
        user=request.user, 
        message='File uploaded successfully', 
        application='file_manager',
        redirect_url='/files/'
    )
    return redirect('file_list')