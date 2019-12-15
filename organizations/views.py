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

    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")

    for detail in u_details:
        if (detail.role_id == 1):
            admins.append(detail.user)
        else:
            users.append(detail.user)

    is_admin = False
    if (is_signed_in):
        ud = request.user.userdetail_set.all().first()
        is_admin = ud.role_id == 1
        
    context = {
        "users": users,
        "admins": admins,
        "org": org,
        "is_admin": is_admin
    }
    return render(request, "details.html", context)