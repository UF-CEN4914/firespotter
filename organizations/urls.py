from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.show, name="show"),
    path("<int:pk>/details", views.details, name="details"),
    path("<int:pk>/create_user", views.create_user, name="create_user"),
    path("details", views.details_redirect, name="details_redirect")
]