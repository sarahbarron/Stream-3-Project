from django.conf.urls import url, include
from .views import register_customer, login_customer, logout_customer, customer_profile, edit_profile
from accounts import urls_reset

#ACCOUNTS APP URLS

#list of url patterns for customer accounts 

urlpatterns = [
    # url for when a user wants to log out 
    url(r'^logout/', logout_customer, name="logout_customer"),
    
    # url for when a user wants to log in
    url(r'^login/', login_customer, name="login_customer"),
    
    # url for when a user wants to register
    url(r'^register/', register_customer, name="register_customer"),
    
    # url for when a user wants to view their profile or check an order status
    url(r'^profile/', customer_profile, name="customer_profile"  ),
    
    # url for a user to edi their user profile 
    url(r'^edit_profile/', edit_profile, name="edit_profile"  ),
    
    # url needed as django automatically adds this link to their Edit Profile form to change a password
    url(r'^password/', include(urls_reset)),
    
    # url for a user to reset their password
    url(r'^password_reset/', include(urls_reset))
    ]