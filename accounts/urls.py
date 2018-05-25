from django.conf.urls import url
from .views import register_customer, login_customer, logout_customer

#ACCOUNTS APP URLS

#url patterns

urlpatterns = [
    url(r'^logout/$', logout_customer, name="logout_customer"),
    url(r'^login/$', login_customer, name="login_customer"),
    url(r'^register/$', register_customer, name="register_customer"),
    ]