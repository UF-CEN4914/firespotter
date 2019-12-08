from django.shortcuts import render

# Create your views here.
def root(request):
  return render(request, 'root.html', {})

def about(request):
  return render(request, 'about.html', {})

def contact(request):
  return render(request, 'contact.html', {})