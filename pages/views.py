from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def root(request):
  return render(request, 'root.html', {})

def about(request):
  return render(request, 'about.html', {})

def contact(request):
  return render(request, 'contact.html', {})

def sign_up(request):
  form = SignupForm()
  
  context = {
    "form": form
  }
  return render(request, 'sign_up.html', context)