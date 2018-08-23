from django.shortcuts import render
from .models import Product

# returns all products 
def all_products(request):
    
    # returns all products that are in stock
    in_stock_products = Product.objects.filter(available_stock__gt = 0)
     
    # returns all products that are out of stock
    out_of_stock_products = Product.objects.filter(available_stock__lte = 0)
    
    # sends both filters to be viewed on the products.html page
    return render(request, 'products.html', {"in_stock_products": in_stock_products, "out_of_stock_products": out_of_stock_products})
     
