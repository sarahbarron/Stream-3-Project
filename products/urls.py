from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    
    # url to view all products
    url(r'^$', all_products, name='all_products'),
    ]