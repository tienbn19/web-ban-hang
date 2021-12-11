from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    type = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)
    img = models.CharField(max_length=255, null=True, blank=True, default=None)
    manufacture = models.CharField(default='', max_length=255)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    discount = models.CharField(default='', max_length=100)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(null=False, blank=False)
    Created_at = models.DateTimeField(auto_now_add=True)