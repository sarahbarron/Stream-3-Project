from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
# Create your views here.

# logout customer
def logout_customer(request):
    
    auth.logout(request)
    messages.success(request, "You have logged out successfully. We hope to see you again soon!")
    return redirect(reverse('get_index'))

# def login_customer(request):
    


# def register_customer(request):



# def customer_profile(request):

