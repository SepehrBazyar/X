from django.contrib.auth.models import (
    User as BaseUser,
    AbstractUser,
    AbstractBaseUser,
    UserManager,
)
from django.db import models

# Create your models here.
class CustomUserManager(UserManager):
    def create_user(self, phone_number, email = ..., password = ..., **extra_fields):
        return super().create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email, password, **extra_fields):
        return super().create_superuser(phone_number, email, password, **extra_fields)


class User(AbstractUser):
    # user = models.OneToOneField(BaseUser)
    phone_number = models.CharField(
        unique=True,
        max_length=11,
    )

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.phone_number
        return super().save(*args, **kwargs)
