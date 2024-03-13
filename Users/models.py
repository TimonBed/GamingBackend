# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest')
    )

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='guest')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
