from django.conf.urls import url
from .views import all_products

''' urls for the products app '''

urlpatterns = [
    url(r'^$', all_products, name='all_products')
]
