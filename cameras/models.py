from django.db import models
from organizations.models import Organization

# Create your models here.
class Camera(models.Model):
    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.DO_NOTHING,
    )    
    ip_address = models.CharField(max_length=100)
    refresh_rate_in_minutes = models.DecimalField(max_digits=5, decimal_places=2)
    username = models.TextField() 
    password = models.TextField()
    short_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)