from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig


class TestHomeApp(TestCase):
    ''' test the app name is home '''

    def test_app(self):
        self.assertEqual("home", HomeConfig.name)
