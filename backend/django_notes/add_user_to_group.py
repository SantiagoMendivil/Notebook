"""Summary 

    Add a user to a group from a view and not in the admin site.
    
    1. Add a post method inside the list view of the model
    2. Get the group with the id calling get_object_or_404(Group, pk=self.kwargs['group_id'])
    3. Get the user id that you will be adding to the group
    4. If the user exists then you can try adding it by searching the object
    and then adding him to the group with the group.user_set.add(user) method
"""
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404


class UsersInGroupListView(ListView):
    model = User
    template_name = "users_in_group.html" 
    context_object_name = "users"

    def get_queryset(self):
        self.group = get_object_or_404(Group, pk=self.kwargs['group_id'])
        return self.group.user_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group_name"] = self.group.name
        context["users_not_in_group"] = User.objects.exclude(groups=self.group)  
        return context

    def post(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['group_id'])        
        user_id = request.POST.get("user_id", None)  
        
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                group.user_set.add(user)
                messages.success(request, f"User {user.username} added to group {group.name} successfully.")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
        else:
            messages.error(request, "No user ID provided.")
        
        return redirect('group_users', group_id=group.id)