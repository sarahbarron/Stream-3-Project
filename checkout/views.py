from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

'''
CHECKOUT VIEWS

'''

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    cart = request.session.get('cart', {})

    # if the stock level changed to 0 at checkout this for loop will check for any products in the cart whose quantity was changed to 0 and remove them from the cart. (you can't amend a dictionary during iteration so i had to change the dic)
    for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
            
    
    # if the       
    if request.method=="POST":
        
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                available_stock = product.available_stock - quantity
               
                if available_stock < 0:
                    
                    for id, quantity in cart.items():
                        product = get_object_or_404(Product, pk=id)
                        available_stock = product.available_stock - quantity
                        if available_stock < 0:
                            quantity = product.available_stock
                            available_stock = product.available_stock - quantity
                            
            
                            #we get a cart that exists or and empty 1 if one is not already created
                        cart = request.session.get('cart', {})
                        #we can only adjust if there is something in the cart 
                        #therefore must be greater that 0
                        
                        
                        cart[id] = quantity
                            
                        request.session['cart'] = cart
                        
                    messages.info(request,'We have limited stock available for we have amended your cart to the maximum available at this time. Please check your cart and checkout again once you are happy to do so<br>', extra_tags="safe")
                    
                    return redirect(reverse('view_cart'))
                    break
    
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                available_stock = product.available_stock - quantity
               
                
                # if available_stock < 0:
                    
                #     for id, quantity in cart.items():
                #         product = get_object_or_404(Product, pk=id)
                #         available_stock = product.available_stock - quantity
                #         if available_stock < 0:
                #             quantity = product.available_stock
                #             available_stock = product.available_stock - quantity
                            
            
                #             #we get a cart that exists or and empty 1 if one is not already created
                #         cart = request.session.get('cart', {})
                #         #we can only adjust if there is something in the cart 
                #         #therefore must be greater that 0
                        
                        
                #         cart[id] = quantity
                            
                #         # else:
                #         #     cart.pop(id)
                            
                            
                #         request.session['cart'] = cart
                        
                #     messages.info(request,'We have limited stock available for we have amended your cart to the maximum available at this time. Please check your cart and checkout again once you are happy to do so<br>', extra_tags="safe")
                    
                #     return redirect(reverse('view_cart'))
                #     break
    
                    
                product.available_stock = available_stock    
                product.save()
                total +=quantity * product.price
                
                    
                
                order_line_item = OrderLineItem(order=order, product=product, quantity=quantity)
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total*100), 
                    currency="EUR", 
                    description=request.user.email, 
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined: ")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('all_products'))
            
            else:
                messages.error(request, "Sorry there seems to be a problem we are unable to take payment")
        
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
            
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    
    