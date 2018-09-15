from django.apps import apps
from django.test import TestCase
from .apps import ProductsearchConfig


class TestProductSearchApp(TestCase):
    ''' test the productsearch apps name is productsearch '''

    def test_app(self):
        self.assertEqual("productsearch", ProductsearchConfig.name)
