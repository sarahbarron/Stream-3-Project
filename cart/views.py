from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    ''' a view that renders the entire contents of the cart '''
    return render(request, "cart.html")

def add_to_cart(request, id):
    #add a quantity of the specified product to the cart
    
    #when you select the quantity and press submit this takes the quantity from there
    quantity=int(request.POST.get('quantity'))
    
    #gets the cart from the session from a cart that exists or an empty 
    #dictionary if it doesn't exist already
    cart = request.session.get('cart', {})
    
    # what we add is an id and a quantity
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))

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