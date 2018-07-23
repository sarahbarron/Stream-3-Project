from django.test import TestCase
from django.contrib.auth.models import User

class TestItemModel(TestCase):

    def test_user_model(self):
        user = User.objects.create_user(username = 'username', email ='myemail@test.com', first_name='first', last_name='last')
        user.save()
        self.assertEqual(user.username, "username")
        self.assertEqual(user.email, "myemail@test.com")
        self.assertEqual(user.first_name, "first")
        self.assertEqual(user.last_name, "last")
     