from django.conf.urls import url
from .views import logout_customer, login_customer

#ACCOUNTS APP URLS

#url patterns

urlpatterns = [
    url(r'^logout/$', logout_customer, name="logout_customer"),
    url(r'^login/$', login_customer, name="login_customer"),
    ]