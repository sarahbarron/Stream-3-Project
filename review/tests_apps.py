from django.apps import apps
from django.test import TestCase
from .apps import ReviewConfig


class TestReviewApp(TestCase):
    ''' test apps name is review '''

    def test_app(self):
        self.assertEqual("review", ReviewConfig.name)
