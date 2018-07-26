from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from django.conf import settings
from django.contrib.messages import get_messages


class TestCheckOutViews(TestCase):
   

    def test_checkout_view_with_customer_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        
        page = self.client.get("/checkout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
    
    def test_checkout_view_with_no_customer_logged_in(self):
        
        page = self.client.get("/checkout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
       
       
    # check if there is no stock available    
    def test_checkout_where_stock_levels_equals_zero(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login user
        self.client.login(username='username', password='password')
        
        # create a product and save it 
        item = Product(id='1', name="PRODUCT NAME ", available_stock=25, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        item.save()
        
        # add the product and quantity to the cart
        self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        
        # change the available stock to 0 and save it
        item = Product(id='1', name="PRODUCT NAME ", available_stock=0, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        item.save()
        
        # get the stripe publisable key 
        stripe_id = settings.STRIPE_PUBLISHABLE
        
        # post customer details and credit card details
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
        
        # check the page status is ok
        self.assertEqual(page.status_code, 200)
        # check the message status are equal
       
    
    def test_checkout_where_there_is_not_enough_stock(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        
        item = Product(id='1', name="PRODUCT NAME ", available_stock=100, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        item.save()
        
        self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        
        item.available_stock=10
        item.save()
        
        stripe_id = settings.STRIPE_PUBLISHABLE
        
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
        
        self.assertEqual(page.status_code, 200)
        
      

    def test_checkout_where_there_is_enough_stock(self):
       
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        
        item = Product(id='1', name="PRODUCT NAME ", available_stock=100, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        item.save()
        
        self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        
        stripe_id = settings.STRIPE_PUBLISHABLE
        
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
      
        self.assertEqual(page.status_code, 200)