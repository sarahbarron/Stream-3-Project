from django.conf.urls import url
from .views import view_cart, add_to_cart, amend_cart

urlpatterns =[
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
   url(r'^amend/(?P<id>\d+)', amend_cart, name='amend_cart'),
    ]