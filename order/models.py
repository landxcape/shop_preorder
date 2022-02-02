from django.db import models

from customer.models import *
from shop.models import *


class Item(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='orders', on_delete=models.CASCADE)
    items = models.ForeignKey(Item, related_name= 'order', on_delete=models.CASCADE)
    ready = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['customer']

    def __str__(self) -> str:
        return self.customer.name
