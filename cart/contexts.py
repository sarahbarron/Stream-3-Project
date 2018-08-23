from django.shortcuts import get_object_or_404
from products.models import Product

'''
products will not be stored in a database they will only be stored in the session while the customer is logged in, when they log out the cart will be lost
'''

def cart_contents(request):
    """
    the cart contents will be available from any page while the customer is logged in
    """
    
    # an instance of the cart if there is one or an empty cart if not
    cart = request.session.get('cart',{})
    # an empty list to store cart items in
    cart_items =[]
    # total cost initially is 0
    total = 0
    # item_total = 0
    # the number of products in the cart is set to 0 initially
    product_count=0
    # while there are products & quantities in the cart
    for id, quantity in cart.items():
        # get an instance of the product
        product = get_object_or_404(Product, pk=id)
        # add the cost of buying the product(s) to the total
        item_total =  quantity * product.price
        total += quantity * product.price
        # add the quantity to the product count
        product_count += quantity
        # append a dictionary with the id, quantity and product to the cart items list
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'item_total': item_total})
    
    #return a dictionary of the cart items, total cost, and product count
    return{ 'cart_items': cart_items, 'total': total, 'product_count': product_count}