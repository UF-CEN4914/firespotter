from django.shortcuts import render
from .forms import SignupForm, SigninForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from organizations.models import Organization
from user_details.models import UserDetail
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def sign_out(request):
  logout(request)
  return redirect("/")

def root(request):
  form = SigninForm()
  is_signed_in = request.user.is_authenticated

  if (is_signed_in):
    ud = request.user.userdetail_set.all().first()
    return redirect(f"/organization/{ud.organization_id}")        
    
  if (request.method == "POST"):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      user_detail = user.userdetail_set.all().first()
      return redirect(f'/organization/{user_detail.organization_id}')

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
        role_id = 1
      )
      user_detail.user_id = user.id
      user_detail.organization = org
      user_detail.save()

      user = authenticate(request, username=username, password=password)
      login(request, user)

      return redirect(f'/organization/{org.id}')
      
  context = {
    "form": form
  }
  return render(request, 'sign_up.html', context)