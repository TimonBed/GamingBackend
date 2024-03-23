# models.py

import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_gravatar.helpers import get_gravatar_url, has_gravatar
import uuid


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
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_expiration = models.DateTimeField(null=True)

    def generate_verification_token(self):
        self.verification_token = uuid.uuid4()
        self.token_expiration = datetime.datetime.now() + datetime.timedelta(hours=3)
        self.save()

    def gravatar_image(self, size=150):
        if (has_gravatar(self.email)):
            return get_gravatar_url(self.email, size=size)
        else:
            return None

    def __str__(self):
        return self.username
