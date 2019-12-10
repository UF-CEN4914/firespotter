from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    timezone = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)