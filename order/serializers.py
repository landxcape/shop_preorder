from rest_framework import serializers

from drf_writable_nested import WritableNestedModelSerializer

from customer.serializers import CustomerSerializer
from shop.serializers import ShopSerializer

from .models import *


class ItemSerialier(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(WritableNestedModelSerializer):
    customer = CustomerSerializer()
    shop = ShopSerializer()
    items = ItemSerialier(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'
