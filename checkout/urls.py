from django.conf.urls import url
from .views import checkout

urlpatterns =[
    # url to checkout to complete an order
    url(r'^$', checkout, name='checkout'),
    ]