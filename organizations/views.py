from django.shortcuts import render
from organizations.models import Organization
from user_details.models import UserDetail
from django.contrib.auth.models import User
from django.shortcuts import redirect

def show(request, pk):
    org = Organization.objects.get(pk=pk)

    context = {
        "org": org
    }
    return render(request, "show.html", context)

def details(request, pk):
    org = Organization.objects.get(pk=pk)
    u_details = org.userdetail_set.all()
    users = []
    admins = []
    for detail in u_details:
        if (detail.role_id == 1):
            admins.append(detail.user)
        else:
            user.append(detail.user)

    context = {
        "users": users,
        "admins": admins,
        "org": org
    }
    return render(request, "details.html", context)