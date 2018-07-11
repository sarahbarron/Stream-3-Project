from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
from django.core.mail import send_mail

'''
CHECKOUT VIEWS

'''

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    cart = request.session.get('cart', {})

    '''
    if the stock level changed to 0 at checkout this for loop will check for any products in the cart whose quantity was changed to 0 and remove them from the cart. (you can't amend a dictionary during iteration so i had to change the dictionary to a list)
    '''
    for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
            
    # if the method is a POST method       
    if request.method=="POST":
        # form with customer personal details
        order_form = OrderForm(request.POST)
        # form with customer bank details
        payment_form = MakePaymentForm(request.POST)
        
        # if the order form and payment form are valid
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            #set the date to the time right now. (ie. the time the customer submitted their personal & payment details)
            order.date = timezone.now()
            # save the order
            order.save()

            #we get a cart that exists or and empty 1 if one is not already created
            cart = request.session.get('cart', {})
            # the total price initally assigned to 0
            total = 0
            
            # itterate through the products in the cart
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                
                #check to see if stock is available before payment
                is_stock_available = product.available_stock - quantity
                
                # if there is not enough stock available
                if is_stock_available < 0:
                    
                    #iterate through all items in the cart to check if stock is available for all items in the cart before payment
                    for id, quantity in cart.items():
                        # get an instance of the product object
                        product = get_object_or_404(Product, pk=id)
                        # gets the available stock for the product from the database subtracts the quantity needed by the customer
                        is_stock_available = product.available_stock - quantity
                        # if the quantity needed by the customer is less than 0 there is not enough stock 
                        if is_stock_available < 0:
                            # change the quantity requested to the maximum available
                            quantity = product.available_stock
            
                        #we get a cart that exists or and empty 1 if one is not already created
                        cart = request.session.get('cart', {})
                        # assign the value quantity to the product id in the cart
                        cart[id] = quantity
                        # assign cart to the session    
                        request.session['cart'] = cart
                    # send a message to the customer to notify them of the stock limitations and amendments to cart    
                    messages.info(request,'We have limited stock available for we have amended your cart to the maximum available at this time. Please check your cart and checkout again once you are happy to do so<br>', extra_tags="safe")
                    # return to cart.html
                    return redirect(reverse('view_cart'))
                    # break out of the view as there are amendments made to the cart, therefore customer needs to check the amendments before proceeding to checkout again
                    break
            
            # when all products are available iterate through the cart
            for id, quantity in cart.items():
                #get an instance of the product object or 404
                product = get_object_or_404(Product, pk=id)
                # total price equals the quantity multiplied by the product price
                total +=quantity * product.price
                # order line item is the deatails from the order form, the product and the quantity requested
                order_line_item = OrderLineItem(order=order, product=product, quantity=quantity)
                # save this to the database
                order_line_item.save()
            
            # try to take payment
            try:
                #create a stripe customer
                customer = stripe.Charge.create(
                    # stripe deals in cents so multipy total by 100
                    amount = int(total*100), 
                    # currency is EURO
                    currency="EUR", 
                    # description is the logged in customers email address
                    description=request.user.email, 
                    # card details is thet details inputted into the payment form
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            
            # if payment cant be taken throw an error
            except stripe.error.CardError:
                # inform the customer of the error
                messages.error(request, "Your card has been declined: ")
            
            # if the customer has paid
            if customer.paid:
                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    # the new available stock will be the available stock for the product in the database less the quantity being bought by the customer now
                    current_available_stock = product.available_stock
                    new_available_stock = current_available_stock - quantity
                    # assign the new available stock to the product available stock in the database
                    product.available_stock = new_available_stock    
                    # save this to the database
                    product.save()
                # send a message to the customer to say payment has been received
                    
                    # if stock levels go below 10 an email will be sent to Gina to warn her.
                    if current_available_stock > 10 & new_available_stock <= 10:
                        send_mail(
                            'LOW STOCK LEVELS',
                            'STOCK LEVELS RUNNING LOW FOR: %s' %product,
                            'sarahflavinbarron@gmail.com',
                            ['sarahflavin@yahoo.com'],
                            fail_silently=False,
                        )
                        
                messages.success(request, "You have successfully paid")
                # set the cart back to empty
                request.session['cart'] = {}
                # redirect back to products.html
                return redirect(reverse('index'))
            
            else:
                # if payment is not successfull send a message to the customer informing them of this
                messages.error(request, "Sorry there seems to be a problem we are unable to take payment")
        
        # if the forms are invalid
        else:
            # print the payment form errors in the console
            print(payment_form.errors)
            # send a message to the customer informing them of the problems with the payment card
            messages.error(request, "We were unable to take payment with that card!")
    
    # if the method is not a POST method show an empty payment & order form
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    # return to checkout.html with the order form, payment form & STRIPE.PUBLISHABLE key        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    
    