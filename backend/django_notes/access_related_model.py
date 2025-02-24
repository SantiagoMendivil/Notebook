"""Summary 

    This is a view example of how to call a related field in a 
    django model.
    1. We have to first generate the view in form of a class. in 
    this case is a ListView in order to display the elements of a 
    model (User). 
    2. We define the get_queryset method that will allow us to retrieve
    information about the model or the associated models. 
    3. We define the get_context_data method in order to retrieve 
    the information of the queryset or any other information into the 
    template.
    4. Initialize the conext as super().get_context_data(**kwargs)
    5. Generate new context data by calling the context variable with 
    the name of the new context as dictionary and the value should be
    a field retrieved in the get_query_set method
    6. The field group_name is now available as a related field of the User
"""

from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

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
        return context
    
