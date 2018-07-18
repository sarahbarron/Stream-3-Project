from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    
    # url to view what is in the cart
    url(r'^$', view_cart, name='view_cart'),
    
    # url to add a product to the cart
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    
    # url to amend the cart
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    ]