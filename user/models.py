from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, ward_name, password, **other_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first_name')
        if not last_name:
            raise ValueError('Users must have a last_name')
        if not ward_name:
            raise ValueError('Users must have a ward_name')

        user = self.model(
            first_name = first_name, last_name= last_name, username=username, ward_name=ward_name, **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, first_name, last_name, username, ward_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        return self.create_user(first_name, last_name, username, ward_name, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    ward_name = models.CharField(max_length=30)
    assent_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=0, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'ward_name']

    def __str__(self):
        return self.username