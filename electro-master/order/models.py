from typing import Callable
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from item.models import Item
from user.models import CustomerUser
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=CASCADE)
    order_time = models.DateTimeField(auto_now=True)
    delivery_address = models.CharField(default='', max_length=100)
    status = models.CharField(default='', max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)