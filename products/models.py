from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    available_stock = models.PositiveSmallIntegerField(default=0)
    content = RichTextUploadingField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name