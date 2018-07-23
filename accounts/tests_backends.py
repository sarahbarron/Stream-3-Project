from django.test import TestCase
from django.contrib.auth.models import User


class TestAccountsBackend(TestCase):
    
    def test_login_with_email_address(self):
        
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='myemail@test.com', password='password')

        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_login_with_email_address_and_wrong_password(self):
        
        user = User.objects.create_user('username', 'myemail@test.com', 'password')
        self.client.login(username='myemail@test.com', password='wrong')

        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_login_with_email_address_but_inactive_user(self):
        
        user = User.objects.create_user('username', 'myemail@test.com', 'password',is_active=False)
        self.client.login(username='myemail@test.com', password='password')

        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
   