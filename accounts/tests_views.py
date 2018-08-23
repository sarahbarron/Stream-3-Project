from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect, get_object_or_404
from .forms import EditProfileForm
from django.contrib import messages
from django.contrib.messages import get_messages


# Test Registration view
class TestAccountViewsRegister(TestCase):
    
    # test the url returns registration.html with a status 200
    def test_get_register_customer_page(self):
        # url to register a customer
        page = self.client.get("/accounts/register/")
        # check for status code 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is registraion.html page
        self.assertTemplateUsed(page, "registration.html")
    
    # test registering a customer when a user is already logged in 
    def test_register_customer_when_someone_logged_in(self):
        # user created
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # user logged in
        self.client.login(username='username', password='password')
        
        # url to try register a user
        page = self.client.get("/accounts/register/", follow=True)
        
        # check for a status 200
        self.assertEqual(page.status_code, 200)
        
         # check Template Used is index.html
        self.assertTemplateUsed(page, "index.html")
        
        # check theat the stored message is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'You are already logged in! If this is not you please <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/logout/">logout</a> and click register again')
        
    
    # test registering a user with valid input
    def test_registering_a_new_user_with_valid_form_input(self):
        # post input to the register url
        page = self.client.post('/accounts/register/', {'email':'john@email.com','username': 'user', 'password1': 'password', 'password2': 'password'}, follow=True)
        # check for a status 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html page
        self.assertTemplateUsed(page, "index.html")
        # check theat the stored message is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'Welcome you are now registered')
      
    # test registering a user with invalid input  
    def test_registering_a_new_user_with_invalid_form_input(self):
        # post an invalid form with no password2 inputted 
        page = self.client.post('/accounts/register/', {'email':'john@email.com','username': 'user', 'password1': 'password', 'password2': ''}, follow=True)
        # check for status code 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is registration.html
        self.assertTemplateUsed(page, "registration.html")
        
    
# Test the Login View    
class TestAccountViewsLogin(TestCase):    
    TestCase.maxDiff = None
    
    # test login url directs you to login.html
    def test_get_login_customer_page(self):
        # url to login
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")
    
    # test trying to login when someone is already logged in
    def test_login_view_when_someone_logged_in(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login the user
        self.client.login(username='username', password='password')
        # url to login
        page = self.client.get("/accounts/login/", follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html
        self.assertTemplateUsed(page, "index.html")
        # check theat the stored message is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'You are already logged in! If this is not you <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/logout/">logout</a> and log back in again under your own username')
    
    # test login when you input valid information    
    def test_login_user_with_valid_form_input(self):
        # create a user
        user = User.objects.create_user('user', 'myemail@test.com', 'password')
        # post login input to the login url 
        page = self.client.post('/accounts/login/', {'username': 'user', 'password': 'password'}, follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is index.html
        self.assertTemplateUsed(page, "index.html")
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'WELCOME You have successfully logged in!')
    
    
    # test login when you enter invalid information    
    def test_login_user_with_invalid_form_input(self):
        # create a user
        user = User.objects.create_user('user', 'myemail@test.com', 'password')
        # post login input with the wrong password to the login url
        page = self.client.post('/accounts/login/', {'username': 'user', 'password': 'xxx'}, follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")
        
        
# Test the logout view
class TestAccountViewsLogout(TestCase):         
    
    # test the log out view    
    def test_get_logout_customer_page_when_someone_logged_in(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login the user
        self.client.login(username='username', password='password')
        # logout url
        page = self.client.get("/accounts/logout/", follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html page
        self.assertTemplateUsed(page, "index.html")
         # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'You have logged out successfully.We hope to see you again soon! <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/login/">login</a> again')
        
    # test the logout view when there is no one logged in
    def test_logout_customer_view_when_no_one_logged_in(self):
        # logout url
        page = self.client.get("/accounts/logout/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login page
        self.assertTemplateUsed(page, "login.html")    
        
# Test Profile views        
class TestAccountViewsProfile(TestCase):          
    
    # test profile view when someone is logged in
    def test_get_profile_page_when_someone_logged_in(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login the user
        self.client.login(username='username', password='password')
        # profile url
        page = self.client.get("/accounts/profile/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")
    
    # test profile view when no-one is logged in    
    def test_profile_view_when_no_one_logged_in(self):
        # profile url
        page = self.client.get("/accounts/profile/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")
        
        
# Test Edit Profile views        
class TestAccountViewsEditProfile(TestCase):
    
    # test edit profile page when someone is logged in
    def test_edit_profile_page_when_someone_logged_in(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login user
        self.client.login(username='username', password='password')
        # edit profile url
        page = self.client.get("/accounts/edit_profile/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is editprofile.html page
        self.assertTemplateUsed(page, "editprofile.html")
    
    # test edit profile page when someone is not logged in    
    def test_edit_profile_page_when_someone_is_not_logged_in(self):
        # edit profile url
        page = self.client.get("/accounts/edit_profile/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
         # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")
    
    # test editing the profile with valid ammendments
    def test_edit_profile_with_valid_ammendments(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # login user
        self.client.login(username='username', password='password')
        # edit profile url
        page = self.client.post("/accounts/edit_profile/", {'username':'change','email':'change@change.com', 'user':'user'},follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")
    
    # test editing the profile where someone is already registered with the email address the user wants to change to 
    def test_edit_profile_when_someone_already_has_that_email_address(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # create a second user
        user2 = User.objects.create_user('change', 'change@change.com', 'password')
        # login the first user
        self.client.login(username='username', password='password')
        # post edit profile form details to the edit profile url
        page = self.client.post("/accounts/edit_profile/", {'username':'username','email':'change@change.com', 'user':'user'},follow=True)
         # check Template Used is editprofile.html page
        self.assertTemplateUsed(page, "editprofile.html")
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'Somebody with this email address is already registered please enter a unique email address')
    
    # test editing the profile where someone is already registered with the username the user wants to change to
    def test_edit_profile_when_someone_has_username(self):
        # create a user
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        # create a second user
        user2 = User.objects.create_user('change', 'change@change.com', 'password')
        # login user
        self.client.login(username='username', password='password')
        # post edit user form details to the edit profile url
        page = self.client.post("/accounts/edit_profile/", {'username':'change','email':'myemail@test.com', 'user':'user'},follow=True)
         # check Template Used is editprofile.html page
        self.assertTemplateUsed(page, "editprofile.html")
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]), 'Somebody already has this username please enter a unique username')
       
        