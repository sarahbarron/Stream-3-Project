from django.db import models
from products.models import Product
from django.conf import settings

# Customer Details for an order
class Order(models.Model):
    
    # stores details of the customers full name, telephone number, address, and date of purchase
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    
    # return the id, date and fullname string
    def __str__(self):
        
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    
# Product details for an order
class OrderLineItem(models.Model):
    
    # order status choices
    STATUS = (
        ('Awaiting Dispatch', 'Awaiting Dispatch'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    )
    # the logged in user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='checkout')
    # the customers details from the Order Model
    order = models.ForeignKey(Order, null=False)
    # the ordered product
    product = models.ForeignKey(Product, null=False)
    # the quantity ordered
    quantity = models.IntegerField(blank=False)
    # the status of an order weather it is awaiting to be dispatched, dispatched or delivered
    status = models.CharField(max_length=20, choices=STATUS, default='Awaiting Dispatch')
    
    # retrun the quantity, product name and product price as a string
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
    