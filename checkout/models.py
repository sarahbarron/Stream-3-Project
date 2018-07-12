from django.db import models
from products.models import Product
from django.conf import settings

class Order(models.Model):
   
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    
    def __str__(self):
        
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    

class OrderLineItem(models.Model):
    STATUS = (
        ('Awaiting Dispatch', 'Awaiting Dispatch'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='checkout')
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    status = models.CharField(max_length=20, choices=STATUS, default='Awaiting Dispatch')
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
    