from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from django.conf import settings
from django.contrib.messages import get_messages

# test checkout view
class TestCheckOutViews(TestCase):
   
    # test checkout view when someone is logged in
    def test_checkout_view_with_customer_logged_in(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login the user
        self.client.login(username='username', password='password')
        # checkout url
        page = self.client.get("/checkout/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is checkout.html page
        self.assertTemplateUsed(page, "checkout.html")
    
    # test the checkout view when someone is logged in
    def test_checkout_view_with_no_customer_logged_in(self):
        # checkout url
        page = self.client.get("/checkout/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is login.html page
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
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'We have limited stock available we have amended your cart to the maximum available at this time. <br> Some Items may have been removed due to no stock availability <br> Please check your cart and checkout again once you are happy to do so')
        
        
        
    # test check out where there is not enough stock
    def test_checkout_where_there_is_not_enough_stock(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login user
        self.client.login(username='username', password='password')
        # create a product
        item = Product(name="PRODUCT NAME ", available_stock=100, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        # save product
        item.save()
        # add the quantity needed to the product id in the cart
        self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        # change the available stock to less than quantity in cart
        item.available_stock=10
        # save the product
        item.save()
        # set the strip_id to the publishable stripe id 
        stripe_id = settings.STRIPE_PUBLISHABLE
        
        # post the customer details and credit card details to the checkout form
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
        
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'We have limited stock available we have amended your cart to the maximum available at this time. <br> Some Items may have been removed due to no stock availability <br> Please check your cart and checkout again once you are happy to do so')
        
    # test checkout where there is enough stock  
    def test_checkout_where_there_is_enough_stock(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login the customer
        self.client.login(username='username', password='password')
        # create an Product
        item = Product(name="PRODUCT NAME ", available_stock=100, content="PRODUCT CONTENT", price=30, image="img.jpg", num_of_ratings=1, average_rating=5)
        # save the product
        item.save()
        # add the quantity needed to the product id in the cart
        self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        
        # assign the stripe publishable key to stripe_id
        stripe_id = settings.STRIPE_PUBLISHABLE
        
        # post the product details and credit card details to the checkout url
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
      
        # check the status code is 200 
        self.assertEqual(page.status_code, 200)
         # check Template Used is cart.html page
        self.assertTemplateUsed(page, "index.html")
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'You have successfully paid')