from django.shortcuts import render
from products.models import Product
from django.contrib import messages
# Create your views here.

def search_for_product(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if products:
        return render(request, "allproducts.html", {"products": products})
    else:
        return render(request, "allproducts.html", messages.info(request,  'Sorry but we are unable to find a product matching this description'))