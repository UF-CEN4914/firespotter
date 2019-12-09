from django.shortcuts import render

# Create your views here.
def root(request):
  return render(request, 'root.html', {})

def about(request):
  return render(request, 'about.html', {})

def contact(request):
  return render(request, 'contact.html', {})

def sign_up(request):
  countries_to_regions =  {
    "US": ["Mid West", "California"],
    "BR": ["Amazon"],
    "DRC": ["Grasslands"]
  }
  context = {
    "country_to_region" : countries_to_regions,
    "sample" : "ans"
  }
  return render(request, 'sign_up.html', context)