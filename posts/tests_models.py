from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):
    ''' Test the Post Model '''

    def test_post_model(self):
        ''' test the post model is working '''

        # create a post
        post = Post(title='title',
                    content='content',
                    views="10",
                    tag="tag",
                    category="category",
                    image="img.jpg",
                    view_on_front_page=False)
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

    def test_return_title_as_a_string(self):
        ''' check the string return is the title '''

        title = Post(title='post')
        self.assertEqual("post", str(title))
