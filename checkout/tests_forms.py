from django.test import TestCase
from .forms import OrderForm, MakePaymentForm


class Test_Make_Payment_Form(TestCase):
    def test_a_valid_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':'pk_test_nbWefqblVg8HnYsFmpcld8qj'})
        self.assertTrue(form.is_valid())
    
        
class Test_Order_Form(TestCase):

    def test_a_valid_order_form(self):
        form = OrderForm({'full_name': 'test full name', 'phone_number': '111', 'street_address1': '12', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertTrue(form.is_valid())
    
    def test_an_invalid_orderform_full_name_removed(self):
        form = OrderForm({'full_name': '', 'phone_number': '111', 'street_address1': '12', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_orderform_phone_number_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '', 'street_address1': '12', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_orderform_street_address_1_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
        
    def test_a_valid_orderform_street_address_2_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '111', 'street_address2': '','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertTrue(form.is_valid())
    
    def test_an_invalid_orderform_town_or_city_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '11', 'street_address2': 'test address','town_or_city': '', 'county': 'test', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_orderform_county_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '11', 'street_address2': 'test address','town_or_city': 'test city', 'county': '', 'country': 'test country', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_orderform_country_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '11', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': '', 'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())
    
    def test_a_valid_orderform_postcode_removed(self):
        form = OrderForm({'full_name': 'test name', 'phone_number': '111', 'street_address1': '111', 'street_address2': 'test address','town_or_city': 'test city', 'county': 'test', 'country': 'test country', 'postcode': ''})
        self.assertTrue(form.is_valid())
       