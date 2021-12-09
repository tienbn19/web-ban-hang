from django.db import models

# Create your models here.
class Item(models.Model):
    type = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)
    img = models.CharField(max_length=255, null=True, blank=True, default=None)
    manufacture = models.CharField(default='', max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    discount = models.CharField(default='', max_length=100)