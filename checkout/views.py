from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request): 
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
                    quantity = product.available_stock
                    available_stock = product.available_stock - quantity
                    messages.info(request,"you have bought all available stock we have had to reduce the number of items in your cart to maximum available as a result" , extra_tags="safe")
                    
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
    
    