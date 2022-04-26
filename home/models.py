from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(verbose_name=_("ایمیل"), unique=True)
    phone_number = models.CharField(verbose_name=_("تلفن ثابت"), max_length=11,unique=True, null=True, blank=True)
    mobile_number = models.CharField(verbose_name=_("موبایل"), max_length=11, unique=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email[:self.email.index('@')]


class Address(models.Model):  # users could add extera address
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=200, verbose_name=_("استان"))
    city = models.CharField(max_length=200, verbose_name=_("شهر"))
    area = models.CharField(max_length=200, verbose_name=_("منطقه"), blank=True)
    street = models.CharField(max_length=200, verbose_name=_("خیابان"))
    alley = models.CharField(max_length=200, verbose_name=_("کوچه"), blank=True)
    plaque = models.CharField(max_length=200, verbose_name=_("پلاک"), blank=True)

    def __str__(self):
        return f"{self.state}\ {self.city}\ {self.area}\ {self.street}\ {self.alley}\ {self.plaque}"
