from django.conf.urls import url
from .views import search_for_product

''' productsearch app views '''

urlpatterns = [
    # url to search for products
    url(r'^$', search_for_product, name='search')
]
