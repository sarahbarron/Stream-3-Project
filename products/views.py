from django.shortcuts import render
from .models import Product

# returns all products to the products.html page
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html",{"products": products})
    

