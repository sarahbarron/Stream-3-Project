from django.shortcuts import render, redirect, reverse
from django.contrib import auth
# Create your views here.

def logout_customer(request):
    
    # when a customer selects logout
    auth.logout(request)
    return redirect(reverse('get_index'))