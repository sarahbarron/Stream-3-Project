from django.test import TestCase
from products.models import Product
from django.shortcuts import get_object_or_404

#cart views: view_cart, add_to_cart, adjust_cart

class TestCartViews(TestCase):

    def test_view_cart_view(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    #test to check add_to_cart view - i changed the quantity in the view to 5 for this test
    def test_add_to_cart_view(self):
        item = Product(id=2, name="Product", available_stock="4", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        id = item.id
        cart = {id:5}
        
        page = self.client.post("/cart/add/{0}".format(item.id), data={'quantity': '100', 'cart':cart}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    
    
    #test to check adjust_cart view - I changed the quantity in the view to 5 for this test
    def test_adjust_cart_view(self):
        item = Product(id=1, available_stock="4", name="Product", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        id = item.id
        
        response = self.client.post("/cart/adjust/{0}".format(id), data={"quantity":100}, follow=True)
        item = get_object_or_404(Product, pk=id)
        self.assertEqual(1, id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")
    