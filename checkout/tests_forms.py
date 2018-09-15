from django.test import TestCase
from .forms import OrderForm, MakePaymentForm


class Test_Make_Payment_Form(TestCase):
    ''' test make payment form '''

    def test_a_valid_make_payment_form(self):
        # create a MakePaymentForm with valid input
        form = MakePaymentForm({'credit_card_number': '4242424242424242',
                                'cvv': '111',
                                'expiry_month': '2',
                                'expiry_year': '2019',
                                'stripe_id':
                                'pk_test_nbWefqblVg8HnYsFmpcld8qj'})
        # check the form is valid
        self.assertTrue(form.is_valid())


class Test_Order_Form(TestCase):
    ''' test the oder form '''

    def test_a_valid_order_form(self):
        ''' test valid input to an order form '''

        # create an order form with valid input
        form = OrderForm({'full_name': 'test full name',
                          'phone_number': '111',
                          'street_address1': '12',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # check the form is valid
        self.assertTrue(form.is_valid())

    def test_an_invalid_orderform_full_name_removed(self):
        '''  test an order form with invalid details
        full name removed '''

        # create a form with invalid input
        form = OrderForm({'full_name': '',
                          'phone_number': '111',
                          'street_address1': '12',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # check the form is invalid
        self.assertFalse(form.is_valid())

    def test_an_invalid_orderform_phone_number_removed(self):
        ''' test an order form with invalid details
        phone number removed '''

        # create an order form with no telephone number
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '',
                          'street_address1': '12',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # check the form is not valid
        self.assertFalse(form.is_valid())

    def test_an_invalid_orderform_street_address_1_removed(self):
        ''' test an order form with invalid details
        address 1 removed '''

        # create a form with no address 1
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # check the form is not valid
        self.assertFalse(form.is_valid())

    def test_a_valid_orderform_street_address_2_removed(self):
        ''' test an order form with valid details
        address 2 removed '''
        # create orderform with valid details
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '111',
                          'street_address2': '',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # test form is valid
        self.assertTrue(form.is_valid())

    def test_an_invalid_orderform_town_or_city_removed(self):
        ''' test an order form with invalid details
        town or city removed'''

        # create order form with town or city removed
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '11',
                          'street_address2': 'test address',
                          'town_or_city': '',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # test form is not valid
        self.assertFalse(form.is_valid())

    def test_an_invalid_orderform_county_removed(self):
        ''' test an order form with invalid details
        county removed '''

        # create order form with no county details
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '11',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': '',
                          'country': 'test country',
                          'postcode': 'test postcode'})
        # check form is not valid
        self.assertFalse(form.is_valid())

    def test_an_invalid_orderform_country_removed(self):
        ''' test an order form with invalid details
        with country removed '''

        # create an order form with country removed
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '11',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': '',
                          'postcode': 'test postcode'})
        # check form is not valid
        self.assertFalse(form.is_valid())

    def test_a_valid_orderform_postcode_removed(self):
        ''' test an order form with valid details
        postcode removed '''

        # create an order form with post code removed
        form = OrderForm({'full_name': 'test name',
                          'phone_number': '111',
                          'street_address1': '111',
                          'street_address2': 'test address',
                          'town_or_city': 'test city',
                          'county': 'test',
                          'country': 'test country',
                          'postcode': ''})
        # check form is valid
        self.assertTrue(form.is_valid())
