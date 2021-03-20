from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url', 'id', 'desired_pizza', 'number_of_pizza',
                  'customer_name', 'customer_number', 'customer_address', 'status')
