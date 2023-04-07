from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class A(models.Model):
    name = models.CharField(max_length=100, default='campo')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='a_set')


class B(models.Model):
    a = models.ForeignKey('A', on_delete=models.PROTECT, null=False)
