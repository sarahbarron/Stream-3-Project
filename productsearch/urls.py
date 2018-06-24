from django.conf.urls import url
from .views import search_for_product

urlpatterns = [
    url(r'^$', search_for_product, name='search')
    ]