from django.db import models

# Create your models here.
class UserDetail(models.Model):
    org_id = models.IntegerField()
    user_id = models.IntegerField()
    role_id = models.IntegerField()