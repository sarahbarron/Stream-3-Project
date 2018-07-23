from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# posts views: get_post, create_or_edit_post, delete_post

class TestPostssViews(TestCase):

    def test_get_post_page(self):
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "allposts.html")
    
    def test_view_full_post_page(self):
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        page = self.client.get("/posts/{0}".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "fullpost.html")
    
    def test_add_post_page(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        self.client.login(username = 'username', password = 'password')
    
        
        page = self.client.get("/posts/new/" , follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
    
    def test_edit_post_page(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        self.client.login(username = 'username', password = 'password')
        
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
    
    def test_to_delete_a_post(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True)
        self.client.login(username = 'username', password = 'password')
        
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "allposts.html")
        
    def test_add_post_page_with_no_one_logged_in(self):
        page = self.client.get("/posts/new/" , follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_edit_post_page_with_no_one_logged_in(self):
        
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_to_delete_a_post_with_no_one_logged_in(self):
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    
    def test_add_post_page_if_logged_in_person_has_no_staff_status(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
    
        
        page = self.client.get("/posts/new/" , follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_edit_post_page_if_logged_in_person_has_no_staff_status(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_to_delete_a_post_if_logged_in_person_has_no_staff_status(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        post = Post(title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        page = self.client.get("/posts/{0}/delete/".format(post.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    
    def test_post_a_new_post(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True, )
        #login the user
        self.client.login(username = 'username', password = 'password')
       
        # post the review data
        self.client.post("/posts/new/", {'title':'Title', 'content':'content', 'category':'test category', 'tag':'test tag', 'view_on_front_page': 'True'},follow=True)
    
    def test_post_edit_post(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password', is_staff=True, )
        #login the user
        self.client.login(username = 'username', password = 'password')
       
        post = Post(id=1, title="Title", content='content', category = 'test category', tag = 'test tag', view_on_front_page= 'True')
        post.save()
        
        # post the review data
        self.client.post("/posts/edit/{0}".format(post.id), {'title':'change', 'content':'change', 'category':'change', 'tag':'change', 'view_on_front_page': 'False'},follow=True)