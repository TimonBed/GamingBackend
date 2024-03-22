# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_gravatar.helpers import get_gravatar_url, has_gravatar


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest')
    )

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='guest')
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def gravatar_image(self, size=150):
        if (has_gravatar(self.email)):
            return get_gravatar_url(self.email, size=size)
        else:
            return None

    def __str__(self):
        return self.username
