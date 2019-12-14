from django.urls import path
from . import views

urlpatterns = [
    path("organization/<int:pk>/", views.show, name="show"),
]