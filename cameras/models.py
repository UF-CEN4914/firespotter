from django.db import models

# Create your models here.
class Camera(models.Model):
    org_id = models.IntegerField()
    ip_address = models.CharField(max_length=100)
    refresh_rate_in_minutes = models.DecimalField(max_digits=5, decimal_places=2)
    username = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)