from django.test import TestCase
from .forms import BlogPostForm

class Test_Blog_Post_Form(TestCase):

    def test_a_valid_blog_post_form(self):
        form = BlogPostForm({'title': 'test title', 'content': 'test content', 'category': 'test category','tag': 'test tag', 'view_on_front_page': 'True', 'published_date': '11/09/2018', 'image': 'img.jpg'})
        self.assertTrue(form.is_valid())