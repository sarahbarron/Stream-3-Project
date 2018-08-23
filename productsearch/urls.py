from django.conf.urls import url
from .views import search_for_product

urlpatterns = [
    # url to search for products
    url(r'^$', search_for_product, name='search')
    ]