from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .UserManager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(unique=True, max_length=14, primary_key=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=150, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()
