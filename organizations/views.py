from django.shortcuts import render
from django.http import HttpResponseRedirect
from organizations.models import Organization
from user_details.models import UserDetail
from django.contrib.auth.models import User
from .forms import UserForm

from django.shortcuts import redirect

def show(request, pk):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != pk):
        return redirect(f"/organization/{ud.organization_id}")

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
        
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != pk):
        return redirect(f"/organization/{ud.organization_id}")

    is_admin = ud.role_id == 1

    for detail in u_details:
        if (detail.role_id == 1):
            admins.append(detail.user)
        else:
            users.append(detail.user)
        
    form = UserForm()
    context = {
        "users": users,
        "admins": admins,
        "org": org,
        "is_admin": is_admin,
        "form": form
    }
    return render(request, "details.html", context)

def profile(request, oid, uid):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != oid or ud.user_id != uid):
        return redirect(f"/organization/{ud.organization_id}/profile/{ud.user_id}")

    form = UserForm()
    form['first_name'].initial = ud.user.first_name
    form['last_name'].initial = ud.user.last_name
    form['email'].initial = ud.user.email
    context = {
        "form": form,
    }
    return render(request, "profile.html", context)

    

def details_redirect(request):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    return redirect(f"/organization/{ud.organization_id}/details")

def profile_redirect(request):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    return redirect(f"/organization/{ud.organization_id}/profile/{ud.user_id}")

def create_user(request, pk):
    if (request.method == "POST"):
        form = UserForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username,
                form.cleaned_data['email'], 
                password 
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_detail = UserDetail (
                role_id = form.cleaned_data['admin_select']
            )
            user_detail.user_id = user.id
            user_detail.organization = Organization.objects.get(pk=pk)
            user_detail.save()
            
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)