from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    available_stock = models.PositiveSmallIntegerField(default=0)
    content = RichTextUploadingField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    num_of_ratings = models.DecimalField(default=0, max_digits=3, decimal_places=0)
    average_rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    
    
    def __str__(self):
        return self.name