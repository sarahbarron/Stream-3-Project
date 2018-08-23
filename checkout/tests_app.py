from django.apps import apps
from django.test import TestCase
from .apps import CheckoutConfig

# check app name is checkout
class TestCheckoutApp(TestCase):
    def test_app(self):
        self.assertEqual("checkout", CheckoutConfig.name)