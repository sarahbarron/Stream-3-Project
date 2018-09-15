from django.db import models
from products.models import Product
from django.conf import settings
from django.utils import timezone

'''
REVIEW MODEL
'''


class Review(models.Model):
    # Product ratings choices from 1 to 5
    RATING_CHOICES = ((1, '1'),
                      (2, '2'),
                      (3, '3'),
                      (4, '4'),
                      (5, '5'))
    # would you recommend to a friend choices Yes or No
    YES_NO = (('YES', 'YES'),
              ('NO', 'NO'))
    # the product being reviewed
    product = models.ForeignKey(Product,
                                null=True,
                                related_name='reviews')
    # the user creating the review
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             related_name='reviews')
    # the title of the review
    title = models.CharField(max_length=200, blank=False)
    # the review comment or message
    comment = models.TextField(null=True, blank=False)
    # the rating of the product between 1 and 5
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    # would you recommend the product to a friend yes or no
    would_you_recommend_to_a_friend = models.CharField(max_length=3,
                                                       choices=YES_NO,
                                                       default='YES')
    # the date the review was made
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.title, self.rating)
