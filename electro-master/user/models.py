from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class CustomerUser(AbstractBaseUser):
    Phone_number = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=100)
class EmployeesUser(AbstractBaseUser):
    Phone_number = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=100)