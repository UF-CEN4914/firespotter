from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.show, name="show"),
    path("<int:pk>/details", views.details, name="details"),
    path("<int:pk>/create_user", views.create_user, name="create_user"),
    path("details", views.details_redirect, name="details_redirect"),
    path("profile", views.profile_redirect, name="profile_redirect"),
    path("<int:oid>/profile/<int:uid>", views.profile, name="profile")
]