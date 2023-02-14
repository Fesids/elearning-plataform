from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("A user must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("A super-user must have an email")

        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class CustomUserModel(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email


