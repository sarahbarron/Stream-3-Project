from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig


# test the app name is home
class TestHomeApp(TestCase):
    def test_app(self):
        self.assertEqual("home", HomeConfig.name)