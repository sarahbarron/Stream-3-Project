from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Product Model - stores details of products 
class Product(models.Model):
    
    # name of product
    name = models.CharField(max_length=254, default='')
    
    # quantity of stock available for the product
    available_stock = models.PositiveSmallIntegerField(default=0)
    
    # description of the product
    content = RichTextUploadingField(blank=True, null=True)
    
    # price of the product
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # image of the product
    image = models.ImageField(upload_to='images')
    
    # number of times a review has been left for the product
    num_of_ratings = models.DecimalField(default=0, max_digits=3, decimal_places=0)
    
    # average rating for the product
    average_rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    
    
    def __str__(self):
        return self.name