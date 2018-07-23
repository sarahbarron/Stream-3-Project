from django.test import TestCase
from products.models import Product

class TestSearchForProductViews(TestCase):

    def test_search_for_product_view(self):
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
       
        page = self.client.get("/search/", {'q': 'Product'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    
    def test_search_for_product_view_when_no_match(self):
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
       
        page = self.client.get("/search/", {'q': 'Hello'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    