from django.test import TestCase


class TestProductsViews(TestCase):
    ''' test the product views '''

    def test_view_to_view_all_products(self):
        ''' test view all_products '''

        # products url
        page = self.client.get("/products/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the Template used is products.html
        self.assertTemplateUsed(page, "products.html")
