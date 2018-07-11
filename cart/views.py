from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages
'''
CART VIEWS

'''

def view_cart(request):
    ''' 
    a view that renders the entire contents of the cart 
    '''
    return render(request, "cart.html")


def add_to_cart(request, id):
    '''
    add a quantity of the specified product to the cart
    when you select the quantity and press add the product id & quantity are added to the cart dictionary
    '''
    # gets the quantity inputted by the customer
    quantity=int(request.POST.get('quantity'))
    # gets the product object or 404 
    product = get_object_or_404(Product, pk=id)
    # we get a cart that exists or and empty 1 if one is not already created
    cart = request.session.get('cart', {})
    
    # if the product is already in the cart add the quantity in the cart to the new customer inputted quantity 
    if id in cart:
        quantity = cart.get(id) + quantity
    
    # checks to see if there is available stock 
    is_stock_available = product.available_stock - quantity
    
    # if there is not enough stock
    if is_stock_available < 0:
        # set the new quantity to the maximum available stock
        quantity = product.available_stock
        # send a message to the customer to tell them the maximum available
        messages.info(request,'%s is the maximum quantity we have at this time we have amended your cart to the maximum available '% quantity , extra_tags="safe")
    
    # add the value quantity to the cart key
    cart[id] = quantity
    #assign cart to the session
    request.session['cart'] = cart
    # redirect back to all products
    return redirect(reverse('all_products'))


def adjust_cart(request, id):
    '''
    adjust the quantity of the product to the specified amount
    gets the existing quantity as an integer
    '''
    # gets the quantity inputted by the customer
    quantity = int(request.POST.get('quantity'))
    # gets the product object or 404
    product = get_object_or_404(Product, pk=id)

    #check to see if stock is available
    is_stock_available = product.available_stock - quantity
    
    # if there is not enough stock available
    if is_stock_available < 0:
        #amend  the quantity to the maximum available stock
        quantity = product.available_stock
        # send a message to the customer informing them of the stock levels and amendment
        messages.info(request,'%s is the maximum quantity we have at this time we have amended your cart to the maximum available '% quantity , extra_tags="safe")
    
    # we get a cart that exists or and empty 1 if one is not already created
    cart = request.session.get('cart', {})
    # we can only adjust if there is something in the cart 
    # therefore quantity must be greater that 0
    if quantity > 0:
        cart[id] = quantity
    # otherwise the quantity is 0 or less therefore remove the item from the cart
    else:
        cart.pop(id)
    
    # assign cart to session 
    request.session['cart'] = cart
    # return to cart.html
    return redirect(reverse('view_cart'))