from django.shortcuts import render
from django.http import HttpResponseRedirect
from organizations.models import Organization
from user_details.models import UserDetail
from django.contrib.auth.models import User
from cameras.models import Camera
from apis.CameraInterface import CameraInterface

# Create your views here.
def show(request, pk):
    is_signed_in = request.user.is_authenticated
    if (not is_signed_in):
        return redirect("/")
    
    ud = request.user.userdetail_set.all().first()
    camera = Camera.objects.get(pk=pk)
    if (ud.organization_id != camera.organization_id):
        return redirect(f"/organization/{ud.organization_id}")

    context = {
        "org": Organization.objects.get(pk=ud.organization_id),
        "camera_feed": CameraInterface.fetchFeed(camera),
        "camera": camera,
        "is_admin": ud.role_id == 1
    }
    return render(request, "camera_show.html", context)