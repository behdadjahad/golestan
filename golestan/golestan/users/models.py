from django.db import models
from golestan.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin



class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name = "email address",
                              unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )

    first_name = models.CharField(max_length=255,
                                  blank=True,
                                  null=True,
                                  verbose_name="first name")
    last_name = models.CharField(max_length=255,
                                 blank=True,
                                 null=True,
                                 verbose_name="last name")
    account_number = models.CharField(max_length=9,
                                      unique=True,
                                      blank=True,
                                      null=True,
                                      verbose_name="account number")
    phone_number = models.CharField(max_length=11, 
                                    blank=True, 
                                    null=True, 
                                    verbose_name='phone number')
    national_id = models.CharField(max_length=10, 
                                   blank=True, 
                                   null=True, 
                                   verbose_name='national id')
    birth_date = models.DateField(blank=True, 
                                  null=True, 
                                  verbose_name='birth date')
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES,
                              default='N')

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin


