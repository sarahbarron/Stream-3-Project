from django.test import TestCase

class TestProductsViews(TestCase):

    def test_view_to_view_all_products(self):
        page = self.client.get("/products/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    