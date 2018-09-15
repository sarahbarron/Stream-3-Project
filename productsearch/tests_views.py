from django.test import TestCase
from products.models import Product


class TestSearchForProductViews(TestCase):
    ''' test productsearch views '''

    def test_search_for_product_view_with_a_match(self):
        ''' test search for product view with a match '''
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # search url searching for Product
        page = self.client.get("/search/", {'q': 'Product'}, follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is products.html
        self.assertTemplateUsed(page, "products.html")

    def test_search_for_product_view_when_no_match(self):
        ''' test seaarch for product view with no match '''

        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # searh url searching for a non existant product
        page = self.client.get("/search/", {'q': 'Hello'}, follow=True)
        # check the page status is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is products.html
        self.assertTemplateUsed(page, "products.html")
