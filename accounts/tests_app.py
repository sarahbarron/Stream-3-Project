from django.apps import apps
from django.test import TestCase
from .apps import AccountsConfig

class TestAccountsApp(TestCase):
    def test_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
       