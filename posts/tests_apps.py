from django.apps import apps
from django.test import TestCase
from .apps import PostsConfig


class TestPostsApp(TestCase):
    ''' Test the apps name is post '''

    def test_app(self):
        self.assertEqual("posts", PostsConfig.name)
