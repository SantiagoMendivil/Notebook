"""Permissions to access a specific view

If the view that you want to restrict to pass a certain method is just a method 
then you must import user_passes_test. But if it is a class import UserPassesTestMixib.
"""
from django.shortcuts import redirect, render
# For method views 
from django.contrib.auth.decorators import user_passes_test
# For class views 
from django.contrib.auth.mixins import UserPassesTestMixin

""" 
Step 1: Create the unauthorized template
    In order to redirect the user to a view when the condition is not 
    met, you must define it along with the template and the url
"""
def unauthorized_user(request):
    return render(request, "unauthorized.html")


"""
Step 2: Create the method based views test
    First you must define the condition that you want the views to 
    evaluate against. In the example below you will define a method 
    that checks if the user has the 'superuser' permission.
"""
def is_admin(user):
    return user.is_superuser

""" 
Step 3: Create a class based view test
    For the class views you must define your own class that is going to inherit
    from the UserPassesTestMixin and generate two methods. One for testing
    the condition and the other to handle the users that doens't have permissions
"""
class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return redirect("unauthorized_template")
    
""" 
Step 4: Generate the views that you want to restrict with the method and class 
    In this case for the method view you must specify the decorator @user_passes_test
    and pass as arguments the method created, the login_url that redirects to the 
    unauthorized url and the redirect_field_name that for simplicity it must be set to next. 
    
    For the class views you must inherit from the class created as first argument (Key point)
"""

@user_passes_test(is_admin, login_url="unauthorized_template", redirect_field_name="next")
def restricted_view(request):
    return render(request, "restricted_view.html")

class AdminRequiredView(SuperUserRequiredMixin, TemplateView):
    template_name = "admin_required_view.html"
    