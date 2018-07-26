from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect, get_object_or_404
from .forms import EditProfileForm
from django.contrib import messages
from django.contrib.messages import get_messages



class TestAccountViewsRegister(TestCase):

    def test_get_register_customer_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
    
    def test_register_customer_when_someone_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/register/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'You are already logged in! If this is not you please <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/logout/">logout</a> and click register again')
        
    
    def test_registering_a_new_user_with_valid_form_input(self):
        page = self.client.post('/accounts/register/', {'email':'john@email.com','username': 'user', 'password1': 'password', 'password2': 'password'}, follow=True)
        self.assertTemplateUsed(page, "index.html")
       
        
    def test_registering_a_new_user_with_invalid_form_input(self):
        page = self.client.post('/accounts/register/', {'email':'john@email.com','username': 'user', 'password1': 'password', 'password2': ''}, follow=True)
        self.assertTemplateUsed(page, "registration.html")
    
    
class TestAccountViewsLogin(TestCase):    
    
    def test_get_login_customer_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_login_view_when_someone_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_login_user_with_valid_form_input(self):
        user = User.objects.create_user('user', 'myemail@test.com', 'password')
        page = self.client.post('/accounts/login/', {'username': 'user', 'password': 'password'}, follow=True)
        self.assertTemplateUsed(page, "index.html")
        
    def test_login_user_with_invalid_form_input(self):
        user = User.objects.create_user('user', 'myemail@test.com', 'password')
        page = self.client.post('/accounts/login/', {'username': 'user', 'password': 'xxx'}, follow=True)
        self.assertTemplateUsed(page, "login.html")
        
        
        
class TestAccountViewsLogout(TestCase):         
        
    def test_get_logout_customer_page_when_someone_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_logout_customer_view_when_no_one_logged_in(self):
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")    
        
        
class TestAccountViewsProfile(TestCase):          
    
    def test_get_profile_page_when_someone_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/profile/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_profile_view_when_no_one_logged_in(self):
        page = self.client.get("/accounts/profile/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
        
        
class TestAccountViewsEditProfile(TestCase):
    
    def test_edit_profile_page_when_someone_logged_in(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/edit_profile/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "editprofile.html")
        
    def test_edit_profile_page_when_someone_is_not_logged_in(self):
        page = self.client.get("/accounts/edit_profile/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_edit_profile_with_valid_ammendments(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.post("/accounts/edit_profile/", {'username':'change','email':'change@change.com', 'user':'user'},follow=True)
        self.assertTemplateUsed(page, "profile.html")
    
    def test_edit_profile_when_someone_already_has_that_email_address(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        user2 = User.objects.create_user('change', 'change@change.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.post("/accounts/edit_profile/", {'username':'username','email':'change@change.com', 'user':'user'},follow=True)
        self.assertTemplateUsed(page, "editprofile.html")
    
    def test_edit_profile_when_someone_has_username(self):
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        user2 = User.objects.create_user('change', 'change@change.com', 'password')
        self.client.login(username='username', password='password')
        page = self.client.post("/accounts/edit_profile/", {'username':'change','email':'myemail@test.com', 'user':'user'},follow=True)
        self.assertTemplateUsed(page, "editprofile.html")
       
       
        