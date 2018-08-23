from django.test import TestCase
from .forms import BlogPostForm

# test blog post form
class Test_Blog_Post_Form(TestCase):
    
    # checked the blog post form is valid
    def test_a_valid_blog_post_form(self):
        # create a blog with a blog post form
        form = BlogPostForm({'title': 'test title', 'content': 'test content', 'category': 'test category','tag': 'test tag', 'view_on_front_page': 'True', 'published_date': '11/09/2018', 'image': 'img.jpg'})
        # check the blog post form is valid
        self.assertTrue(form.is_valid())
        