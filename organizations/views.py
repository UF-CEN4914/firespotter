from django.shortcuts import render
from organizations.models import Organization

# Create your views here.
def show(request, pk):
    org = Organization.objects.get(pk=pk)

    context = {
        "org": org
    }
    return render(request, "show.html", context)