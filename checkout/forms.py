from django import forms
from .models import Order


# form for the credit card details when making a payment
class MakePaymentForm(forms.Form):
    # month ranges for expiry date
    MONTH_CHOICES =[(i,i) for i in range (1, 12)]
    # year ranges for expiry date
    YEAR_CHOICES = [(i,i) for i in range (2018, 2030)]
    
    # credit card number 
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    
    # 3 digit CVV security number
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    
    # expiry month
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    
    # expiry year
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    
    # stripe id which is hidden from the customer
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta: 
        # form is based on the Order Model 
        model = Order
        # fields to be used in the form
        fields = ('full_name','phone_number', 'street_address1', 'street_address2', 'town_or_city', 'county', 'country','postcode',)
    