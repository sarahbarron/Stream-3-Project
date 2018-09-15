from django.conf.urls import url
from .views import checkout, paid

''' urls for the checkout app '''
urlpatterns = [
    # url to checkout to complete an order
    url(r'^$', checkout, name='checkout'),
    # url to paid.html when an order has been paid
    url(r'^paid/$', paid, name='paid'),
]
