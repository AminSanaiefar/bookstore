from django.db import models
from django.contrib.auth.models import AbstractUser


# to set this model for auth in django we have to define AUTH_USER_MODEL var
# and for this situation set value 'accounts.CustomUser' Cuz app is accounts and class name is CustomUser
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

