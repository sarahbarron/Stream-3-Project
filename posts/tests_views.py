from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# test posts views
class TestPostssViews(TestCase):
    
    # test get post page
    def test_get_post_page(self):
        # posts urls
        page = self.client.get("/posts/")
        # check status code 200
        self.assertEqual(page.status_code, 200)
        # check you are directed to the allposts.html page
        self.assertTemplateUsed(page, "allposts.html")
    
    # test view the full post page
    def test_view_full_post_page(self):
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        #save a post
        post.save()
        # view full post url with post id
        page = self.client.get("/posts/{0}".format(post.id), follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check that you are directed to the fullpost.html page
        self.assertTemplateUsed(page, "fullpost.html")
    
# Test Add Post view    
class TestAddPostView(TestCase):
    # test add post page
    def test_add_post_page(self):
        # create a user with staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        # login the user
        self.client.login(username = 'username', password = 'password')
        # posts new url
        page = self.client.get("/posts/new/" , follow = True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # check the template used is blogpostform.html
        self.assertTemplateUsed(page, "blogpostform.html")
    
    # test add post when no-one is logged in
    def test_add_post_page_with_no_one_logged_in(self):
        # posts new url
        page = self.client.get("/posts/new/" , follow = True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")
    
    # test add post if logged in person does not have staff status
    def test_add_post_page_if_logged_in_person_has_no_staff_status(self):
        # create a user with no staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        # login the user
        self.client.login(username = 'username', password = 'password')
        # posts new url
        page = self.client.get("/posts/new/" , follow = True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is index.html
        self.assertTemplateUsed(page, "index.html")
    
    # test posting to a new post view
    def test_post_a_new_post(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True, )
        #login the user
        self.client.login(username = 'username', password = 'password')
        # post the post data
        page = self.client.post("/posts/new/", {'title':'Title', 'content':'content', 'category':'test category', 'tag':'test tag', 'view_on_front_page': 'True'},follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is fullpost.html
        self.assertTemplateUsed(page, "fullpost.html")

# Test Edit Post View
class TestEditPostView(TestCase):
    
    # test edit post page
    def test_edit_post_page(self):
        # create a user with staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        # login the user
        self.client.login(username = 'username', password = 'password')
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is blogpostform.html
        self.assertTemplateUsed(page, "blogpostform.html")
    
    # test edit post with no-one logged in
    def test_edit_post_page_with_no_one_logged_in(self):
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is login.html
        self.assertTemplateUsed(page, "login.html")

    # test edit post if person logged in is not a staff member
    def test_edit_post_page_if_logged_in_person_has_no_staff_status(self):
        # create a user with no staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        # login the user
        self.client.login(username = 'username', password = 'password')
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check th template used is index.html
        self.assertTemplateUsed(page, "index.html")
    
    # test posting an edited post 
    def test_post_edit_post(self):
        #create a user with staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True, )
        #login the user
        self.client.login(username = 'username', password = 'password')
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save the post
        post.save()
        # post the post data using the edit post url
        page = self.client.post("/posts/{0}/edit/".format(post.id), {'title':'change', 'content':'change', 'category':'change', 'tag':'change', 'view_on_front_page': 'False'},follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is fullpost.html
        self.assertTemplateUsed(page, "fullpost.html")


# test delete posts
class TestDeletPostView(TestCase):

    # check the delete post view
    def test_to_delete_a_post(self):
        # create a user with staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        # login the user
        self.client.login(username = 'username', password = 'password')
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save the post 
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        # check the error status is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is allposts.html
        self.assertTemplateUsed(page, "allposts.html")
    
    # test to delete post when no-one is logged in
    def test_to_delete_a_post_with_no_one_logged_in(self):
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save a post
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")
    
    # test delete post when someone is logged in with no staff status    
    def test_to_delete_a_post_if_logged_in_person_has_no_staff_status(self):
        # create a user with no staff status
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        # login the user
        self.client.login(username = 'username', password = 'password')
        # create a post
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        # save a post
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is index.html
        self.assertTemplateUsed(page, "index.html")
    