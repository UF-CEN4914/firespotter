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
    u_details = UserDetail.objects.get(id=org.id)