from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    ''' form for the credit card details when making a payment '''

    # month ranges for expiry date
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    # year ranges for expiry date
    YEAR_CHOICES = [(i, i) for i in range(2018, 2030)]
    # credit card details - Stripe deals with the encryption of all our data
    # so we set all our required to False, so that plain
    # text is not transmitted through the browser
    credit_card_number = forms.CharField(label='Credit Card Number',
                                         required=False)
    # 3 digit CVV security number
    cvv = forms.CharField(label='Security code (CVV)',
                          required=False)
    # expiry month
    expiry_month = forms.ChoiceField(label='Month',
                                     choices=MONTH_CHOICES,
                                     required=False)
    # expiry year
    expiry_year = forms.ChoiceField(label='Year',
                                    choices=YEAR_CHOICES,
                                    required=False)
    # stripe id which is hidden from the customer
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    ''' The order form '''
    class Meta:
        # form is based on the Order Model
        model = Order
        # fields to be used in the form
        fields = ('full_name',
                  'phone_number',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'country',
                  'postcode',)
