from django.test import TestCase

# test the product views
class TestProductsViews(TestCase):

    # test view all products
    def test_view_to_view_all_products(self):
        # products url
        page = self.client.get("/products/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the Template used is products.html
        self.assertTemplateUsed(page, "products.html")
    