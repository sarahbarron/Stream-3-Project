from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OrderForm, MakePaymentForm
from products.models import Product
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
    
    def test_post_forms(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
       
        page = self.client.post("/checkout/",{'full_name':'name','phone_number':'123', 'street_address1':'my', 'street_address2':'address is', 'town_or_city':'kk', 'county':'ireland', 'country':'ireland','postcode':'eircode', 'credit_card_number': '4242424242424242','cvv':'111', 'expiry_month':'2','expiry_year':'2019', 'id':'1', 'name':'product', 'available_stock':'100', 'price':'30'}, follow=True)
        
    def test_cart_session(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        
        item = Product(id='1', name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="1", average_rating="5")
        item.save()
        
        item2 = Product(id='2', name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="1", average_rating="5")
        item.save()
        item2.save()
        
        cart = self.client.session
        cart['1'] = 3
        cart['2'] = 1
        cart.save() 
       
        page = self.client.post("/checkout/", follow=True)