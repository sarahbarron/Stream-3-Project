from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig

class TestHomeApp(TestCase):
    def test_app(self):
        self.assertEqual("home", HomeConfig.name)