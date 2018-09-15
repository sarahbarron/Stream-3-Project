from django.shortcuts import render
from products.models import Product
from django.contrib import messages


def search_for_product(request):
    ''' search for a product '''

    # searches for a product in the product model and assigns it to products
    products = Product.objects.filter(name__icontains=request.GET['q'])
    # if a product is found by the search
    if products:
        # return the found product to the products.html page
        return render(request, "products.html", {"products": products})
    else:
        # other wise return to the products.html page with a sorry message.
        return render(request, "products.html",
                      messages.info(request,
                                    'Sorry but we are unable to find a product'
                                    ' matching this description'))
