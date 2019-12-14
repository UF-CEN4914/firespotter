from django.shortcuts import render
from .forms import SignupForm, SigninForm
from django.contrib.auth.models import User
from django.apps import apps
from django.shortcuts import redirect
from organizations.models import Organization
from user_details.models import UserDetail
from user_details.models import UserDetail
from django.contrib.auth import authenticate, login

# Create your views here.
def root(request):
  form = SigninForm()
  if (request.method == "POST"):
    if (form.is_valid()):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        user_detail = UserDetail.objects.get(pk=user.id)
        return redirect(f'/organization/{user_detail.org_id}')

  context = {
    "form": form
  }
  return render(request, 'root.html', context)

def about(request):
  return render(request, 'about.html', {})

def contact(request):
  return render(request, 'contact.html', {})

def sign_up(request):
  form = SignupForm()
  
  if (request.method == "POST"):
    form = SignupForm(request.POST)
    if (form.is_valid()):
      org = Organization(
        name = form.cleaned_data['org_name'],
        country = form.cleaned_data['org_country'],
        region = form.cleaned_data['org_region'],
        email = form.cleaned_data['org_email'],
        phone_num = form.cleaned_data['org_phone_num']
      )
      org.save()

      username = form.cleaned_data['admin_email']
      password = form.cleaned_data['admin_password']
      user = User.objects.create_user(
        username,
        form.cleaned_data['admin_email'], 
        password 
      )
      user.first_name = form.cleaned_data['admin_first_name']
      user.last_name = form.cleaned_data['admin_last_name']
      user.save()

      user_detail = UserDetail (
        user_id = user.id,
        org_id = org.id,
        role_id = 1
      )
      user_detail.save()

      user = authenticate(request, username=username, password=password)
      login(request, user)

      return redirect(f'/organization/{org.id}')
      
  context = {
    "form": form
  }
  return render(request, 'sign_up.html', context)