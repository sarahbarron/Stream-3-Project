from django.conf.urls import url, include
from .views import register_customer, login_customer, logout_customer, customer_profile, edit_profile
from accounts import urls_reset

#ACCOUNTS APP URLS

#list of url patterns for customer accounts 

urlpatterns = [
    url(r'^logout/', logout_customer, name="logout_customer"),
    url(r'^login/', login_customer, name="login_customer"),
    url(r'^register/', register_customer, name="register_customer"),
    url(r'^profile/', customer_profile, name="customer_profile"  ),
    url(r'^edit_profile/', edit_profile, name="edit_profile"  ),
    url(r'^password/', include(urls_reset)),
    url(r'^password_reset/', include(urls_reset))
    ]