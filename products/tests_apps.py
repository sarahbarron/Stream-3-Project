from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig


class TestProductsApp(TestCase):
    ''' test the app is products '''

    def test_app(self):
        self.assertEqual("products", ProductsConfig.name)
