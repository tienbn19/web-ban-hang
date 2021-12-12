from typing import Tuple
from django.db import models

# Create your models here.

class items(models.Model):
    type = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)
    img = models.CharField(max_length=255, null=True, blank=True, default=None)
    manufacture = models.CharField(default='', max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

class employees(models.Model):
    username = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=100)
    full_name = models.CharField(default='', null=True, max_length=100)
    dob = models.DateField(default='', null=True, max_length=100)
    address = models.CharField(default='', null=True, max_length=100)
    phone_number = models.IntegerField(default='', null=True)
    email = models.CharField(default='', null=True, max_length=50)
    roles = models.CharField(default='01', max_length=2)
