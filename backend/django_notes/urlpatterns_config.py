from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'onlinecourse'
urlpatterns = [
    # Add paths here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)