from config.settings import STATIC_URL
from django.db import models
from django.db.models.fields import IntegerField


class Order(models.Model):
    PIZZA_SIZES = [
        ('L', "Large"),
        ('M', "Medium"),
        ('S', "Small")
    ]
    STATUS = [
        ('ORDER RECEVIED', 'Order Received'),
        ('ORDER PLACED', 'Order Placed'),
        ('OUT FOR DELIVERY', 'Out For Delivery'),
        ('DELIVERED', 'Delivered')
    ]
    desired_pizza = models.CharField(max_length=50)
    number_of_pizza = models.IntegerField()
    size = models.CharField(
        max_length=30, choices=PIZZA_SIZES, default="Large")
    customer_name = models.CharField(max_length=50)
    customer_number = IntegerField()
    customer_address = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return self.desired_pizza
