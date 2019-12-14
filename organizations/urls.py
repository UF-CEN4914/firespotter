from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.show, name="show"),
    path("<int:pk/details", views.details, name="details")
]