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
    
    #when you select the quantity and press submit this takes the quantity from there
    quantity=int(request.POST.get('quantity'))
    

    product = get_object_or_404(Product, pk=id)
                
    available_stock = product.available_stock - quantity
                
    if available_stock < 0:
        quantity = product.available_stock
        available_stock = product.available_stock - quantity
        messages.info(request,"there is not enough please we have amended the quantity to the max available")
            
    cart = request.session.get('cart', {})
    
    # what we add is an id and a quantity
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('all_products'))

def adjust_cart(request, id):
    #adjust the quantity of the product to the specified amount
    
    #gets the existing quantity as an integer
    quantity = int(request.POST.get('quantity'))
    
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