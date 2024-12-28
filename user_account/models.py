from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=125, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    date_joined = models.DateField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    def __str__(self) -> str:
        return self.email
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
