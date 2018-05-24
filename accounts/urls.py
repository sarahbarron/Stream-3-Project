from django.conf.urls import url
from .views import logout_customer

#ACCOUNTS APP URLS

#url patterns

urlpatterns = [
    url(r'^logout/$', logout_customer, name="logout_customer")
    ]