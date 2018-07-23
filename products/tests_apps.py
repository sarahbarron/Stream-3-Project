from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig

class TestProductsApp(TestCase):
    def test_app(self):
        self.assertEqual("products", ProductsConfig.name)