from django.test import TestCase
from products.models import Product
from django.shortcuts import get_object_or_404

# test cart views
class TestCartViews(TestCase):
    
    # test viewing a cart
    def test_view_cart_view(self):
        # view a cart url
        page = self.client.get("/cart/")
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")
        
    #test to check add_to_cart view - i changed the quantity in the view to 5 for this test
    def test_add_to_cart_view(self):
        # create a Product
        item = Product(name="Product", available_stock="4", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '20'}, follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is products.html
        self.assertTemplateUsed(page, "products.html")
    
    
    #test adjusting the cart view
    def test_adjust_cart_view(self):
        # create an item
        item = Product(available_stock="4", name="Product", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the item
        item.save()
        # post the product id and ammended quantity
        page = self.client.post("/cart/adjust/{0}".format(item.id), data={"quantity":100}, follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        #  # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")
    
    
    
    
    
    