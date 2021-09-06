from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):  # custom user instead user django
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'auth_user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class UserAddress(models.Model):  # users can add extera address
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
