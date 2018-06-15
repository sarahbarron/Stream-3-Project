from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """ view that renders all the contents of the cart_contents"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """ Add a quantity of the specified products to the cart """
    
    quantity = int(request.POST.get('quantity'))
    
    #will get the cart of the session
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    

def amend_cart(request):
    """ view to amend a carts contents """
    quantity = int(request.POST.get('quantity'))
    
    #will get the cart of the session
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))