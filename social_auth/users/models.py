from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('agent', 'Agent'),
        ('football_player', 'Football Player'),
    ]

    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='coach')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
