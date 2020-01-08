from django.shortcuts import render
from django.http import HttpResponseRedirect
from organizations.models import Organization
from user_details.models import UserDetail
from cameras.models import Camera
from django.contrib.auth.models import User
from .forms import UserForm
from cameras.forms import CameraForm
from apis.CameraInterface import CameraInterface
from apis.FireChecker import FireChecker
from apis.models.CameraInstance import CameraInstance
from django.http import JsonResponse

from django.shortcuts import redirect

def show(request, pk):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
    
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != pk):
        return redirect(f"/organization/{ud.organization_id}")

    org = Organization.objects.get(pk=pk)

    cameras = org.camera_set.all()
    camera_instances = []

    for camera in cameras:
        camera_instance = CameraInstance()
        camera_instance.ip_address = camera.ip_address
        camera_instance.image_path = CameraInterface.fetchFrame(camera)
        camera_instance.is_on_fire = FireChecker.IsWildFire(camera_instance.image_path)
        camera_instance.short_name = camera.short_name
        camera_instance.cid = camera.id
        
        camera_instances.append(camera_instance)

    context = {
        "org": org,
        "cameras": camera_instances,
        "form": CameraForm()
    }

    return render(request, "show.html", context)

def details(request, pk):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != pk):
        return redirect(f"/organization/{ud.organization_id}")

    is_admin = ud.role_id == 1
    org = Organization.objects.get(pk=pk)
    u_details = org.userdetail_set.all()
    users = []
    admins = []

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
        "org": Organization.objects.get(pk=oid)
    }
    return render(request, "profile.html", context)

def fetch_frame(request, oid, cid, time):
    org = Organization.objects.get(pk=oid)
    camera = Camera.objects.get(pk=cid)
    image_path = CameraInterface.fetchFrame(camera)
    should_update = False
    refresh_rate = camera.refresh_rate_in_minutes
    if (time % refresh_rate == 0):
        should_update = True

    data = { 
        "ip_address": camera.ip_address,
        "image_path": image_path,
        "is_on_fire": FireChecker.IsWildFire(image_path),
        "short_name": camera.short_name,
        "should_update": should_update,
        "cid": camera.id,
        "oid": org.id
    }
    return JsonResponse(data)

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

def update_user(request, oid, uid):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
        
    ud = request.user.userdetail_set.all().first()
    if (ud.organization_id != oid or ud.user_id != uid):
        return redirect(f"/organization/{ud.organization_id}/profile/{ud.user_id}")

    if (request.method == "POST"):
        form = UserForm(request.POST)
        form.is_valid()
        user = User.objects.get(pk=uid)

        user.username = form.cleaned_data['email']
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.first_name = first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
            
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)