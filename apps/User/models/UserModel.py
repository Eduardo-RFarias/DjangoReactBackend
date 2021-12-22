from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_slug
from django.db import models

from ..validators import CpfValidator
from .UserManager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=11,
        validators=[CpfValidator(), validate_slug],
    )
    email = models.EmailField()
    full_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["email", "full_name"]

    objects = UserManager()

    @property
    def todos(self):
        return self.todo_set.all()
