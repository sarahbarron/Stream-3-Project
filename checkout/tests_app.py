from django.apps import apps
from django.test import TestCase
from .apps import CheckoutConfig


class TestCheckoutApp(TestCase):
    ''' test the app name is checkout '''

    def test_app(self):
        self.assertEqual("checkout", CheckoutConfig.name)
