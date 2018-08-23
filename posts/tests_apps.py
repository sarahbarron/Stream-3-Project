from django.apps import apps
from django.test import TestCase
from .apps import PostsConfig

# test app name is post
class TestPostsApp(TestCase):
    def test_app(self):
        self.assertEqual("posts", PostsConfig.name)