from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig

# test the product app return the string products
class TestProductsApp(TestCase):
    def test_app(self):
        self.assertEqual("products", ProductsConfig.name)