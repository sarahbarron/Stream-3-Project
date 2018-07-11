from django.db import models
from products.models import Product
from django.conf import settings
from django.utils import timezone


'''
Review Model
'''

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    YES_NO = (
        (True, 'YES'),
        (False, 'NO')
    )
   
    product = models.ForeignKey(Product, null=True, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='reviews')
    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    would_you_recommend_to_a_friend = models.BooleanField(choices=YES_NO)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return "{0}-{1}".format(self.title, self.rating)


    