from django.test import TestCase
from products.models import Product

# test search for product views
class TestSearchForProductViews(TestCase):
    
    # test search for product view
    def test_search_for_product_view(self):
        # create a product
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        # search url searching for Product
        page = self.client.get("/search/", {'q': 'Product'}, follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is products.html
        self.assertTemplateUsed(page, "products.html")
    
    # test seaarch for product view with no match
    def test_search_for_product_view_when_no_match(self):
        # create a product
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        # searh url searching for a non existant product
        page = self.client.get("/search/", {'q': 'Hello'}, follow=True)
        # check the page status is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is products.html
        self.assertTemplateUsed(page, "products.html")
    