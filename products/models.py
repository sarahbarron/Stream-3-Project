from django.db import models


class Product(models.Model):
    ''' Product Model - stores details of products '''

    # name of product
    name = models.CharField(max_length=100, default='')
    # description of the product
    content = models.TextField(max_length=200, blank=True)
    # price of the product
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image of the product
    image = models.ImageField(upload_to='images')
    # number of times a review has been left for the product
    num_of_ratings = models.DecimalField(default=0,
                                         max_digits=3,
                                         decimal_places=0)
    # average rating for the product
    average_rating = models.DecimalField(default=0,
                                         max_digits=3,
                                         decimal_places=1)
    # quantity of stock available for the product
    available_stock = models.PositiveSmallIntegerField(default=0)

    # return the name
    def __str__(self):
        return self.name
