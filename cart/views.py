from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages
'''
CART VIEWS

'''

def view_cart(request):
    ''' a view that renders the entire contents of the cart '''
    return render(request, "cart.html")

def add_to_cart(request, id):
    #add a quantity of the specified product to the cart
    #when you select the quantity and press add the product id & quantity are added to the cart dictionary
    
    # assigns the quantity to the inputed quantity from the customer
    quantity=int(request.POST.get('quantity'))
    # assign the products object to product or 404 status 
    product = get_object_or_404(Product, pk=id)
    # is_stock_available assigned to the products available stock - the inputed quantity
    is_stock_available = product.available_stock - quantity
    # if the is_stock_available less than zero (i.e there is not enough stock)
    if is_stock_available < 0:
        # set the new quantity to the maximum available stock
        quantity = product.available_stock
        # send a message to the customer to tell them the maximum available
        messages.info(request,'%s is the maximum quantity we have at this time we have amended your cart to the maximum available '% quantity , extra_tags="safe")
    # get an instance of the cart or an empty cart if there is none
    cart = request.session.get('cart', {})
    # add an id and a quantity to the cart
    cart[id] = cart.get(id, quantity)
    #assign cart to the session
    request.session['cart'] = cart
    # redirect back to all products
    return redirect(reverse('all_products'))

def adjust_cart(request, id):
    #adjust the quantity of the product to the specified amount
    #gets the existing quantity as an integer
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    available_stock = product.available_stock - quantity
    if available_stock < 0:
        quantity = product.available_stock
        available_stock = product.available_stock - quantity
        messages.info(request,'%s is the maximum quantity we have at this time we have amended your cart to the maximum available '% quantity , extra_tags="safe")
    #we get a cart that exists or and empty 1 if one is not already created
    cart = request.session.get('cart', {})
    #we can only adjust if there is something in the cart 
    #therefore must be greater that 0
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))