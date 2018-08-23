from django.test import TestCase
from .models import Post

# test the post model
class TestPostModel(TestCase):

    # check the post model
    def test_post_model(self):
        # create a post
        post = Post(title = 'title', content ='content', views="10", tag = "tag", category = "category", image = "img.jpg", view_on_front_page=False)
        # save the post
        post.save()
        # check the post model fields are equal to the created post
        self.assertEqual(post.title, "title")
        self.assertEqual(post.content, "content")
        self.assertEqual(post.views, "10")
        self.assertEqual(post.tag, "tag")
        self.assertEqual(post.category, "category")
        self.assertEqual(post.image, "img.jpg")
        self.assertFalse(post.view_on_front_page)
    
    # check the string return is post
    def test_return_title_as_a_string(self):
        title = Post(title='post')
        self.assertEqual("post", str(title))
        