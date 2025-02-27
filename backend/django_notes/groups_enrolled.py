"""View all groups for a user, including the ones that he/she is enrolled to and those that not

1. Receive as parameter the user_id for an individual view of the groups
2. Retrieve the user's object with the id of the argument
3. Get all groups for the user with user.groups.all()
4. Get all the groups pending for the user with Group.objects.exclue(id__in=groups_enrolled.values_list("id", flat=True))
    4.1. This line excludes the id's selected in groups_enrolled
    4.2. It transforms the queryset to a list of ids
5. Pass the groups_enrolled and groups_pending to the context 
"""
def user_groups(request, user_id):
    user = User.objects.get(id=user_id)
    groups_enrolled = user.groups.all()
    groups_pending = Group.objects.exclude(id__in=groups_enrolled.values_list("id", flat=True))
    context = {
        "user": user, "groups_enrolled": groups_enrolled, "groups_pending": groups_pending
    }
    return render(request, "user_groups.html", context)