from django.apps import apps
from django.test import TestCase
from .apps import CartConfig

class TestCartApp(TestCase):
    def test_app(self):
        self.assertEqual("cart", CartConfig.name)