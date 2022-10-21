from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils.translation import gettext_lazy as _

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     phone= models.CharField(max_length=100)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['']
#     objects =  CustomUserManager()


class Signup(models.Model):
    Users = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    phone_number= models.CharField(max_length=200)
    address= models.CharField(max_length=200)

class Question(models.Model):
    question=models.CharField(max_length=200)

