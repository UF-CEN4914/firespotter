from django.db import models
from organizations.models import Organization
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.DO_NOTHING
    )
    role_id = models.IntegerField()