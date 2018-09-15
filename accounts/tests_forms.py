from django.test import TestCase
from .forms import CustomerRegistrationForm, CustomerLoginForm, EditProfileForm
from django.contrib.auth.models import User


class Test_Customer_Registration_Form(TestCase):
    ''' Test the customer registration form '''

    def test_a_valid_registration_with_just_required_fields(self):
        ''' test registration form with valid
        input into the required fields '''

        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'test',
                                         'password2': 'test', })
        self.assertTrue(form.is_valid())

    def test_valid_registration_with_required_and_unrequired_fields(self):
        ''' test registration form with valid
        input in required and unrequired fields '''

        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'test',
                                         'password2': 'test',
                                         'first_name': 'test first name',
                                         'last_name': 'test last name'})
        self.assertTrue(form.is_valid())

    def test_an_invalid_registration_leaving_out_email_address(self):
        ''' test registration form is invalid
            when the email address is omitted '''

        form = CustomerRegistrationForm({'username': 'test',
                                         'password1': 'test',
                                         'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_username(self):
        ''' test a registration form is
            invalid when username is omitted '''

        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'password1': 'test',
                                         'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_password1(self):
        ''' test registration form is
            invalid if password 1 is omitted '''

        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_password2(self):
        ''' test registration form is invalid if password 2 is omitted '''
        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'test', })
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_email(self):
        ''' Test if the email is not inputted
            the message 'This field is
            required.' is shown '''

        form = CustomerRegistrationForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_correct_message_for_missing_username(self):
        ''' Test if the username is not inputted
            the message 'This field is
            required.' is shown '''

        form = CustomerRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_missing_password1(self):
        ''' Test if the password1 is not inputted
            the message 'This field is
            required.' is shown '''

        form = CustomerRegistrationForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'],
                                    [u'This field is required.'])

    def test_correct_message_for_missing_password2(self):
        ''' Test if the password2 is not inputted
            the message 'This field is
            required.' is shown '''

        form = CustomerRegistrationForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'],
                                    [u'This field is required.'])

    def test_correct_message_for_invalid_email(self):
        ''' Test if the email address does not
            contain @ and . that the message
            'Enter a valid email address.' is shown '''

        form = CustomerRegistrationForm(
            {'email': 'test with invalid email syntax'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                         [u'Enter a valid email address.'])

    def test_when_email_address_is_already_associated_with_another_user(self):
        ''' Test if the inputted email address
            is the same as another users email address
            the message 'Somebody with this email address
            is already registered' is shown '''

        user = User.objects.create_user(username='user',
                                        email='myemail@test.com',
                                        password='password')
        user2 = {'username': 'username',
                 'email': 'myemail@test.com',
                 'password': 'password'}
        form = CustomerRegistrationForm(user2)
        self.assertEqual(form.errors['email'],
                         [u'Somebody with this '
                          'email address is already '
                          'registered'])

    def test_a_invalid_registration_with_different_passwords(self):
        ''' Test that if two passwords inputted
        are not the same the message 'Both passwords
        must be the same' is shown '''

        form = CustomerRegistrationForm({'email': 'test@gmail.com',
                                         'username': 'test',
                                         'password1': 'test',
                                         'password2': 'wrong', })
        self.assertEqual(form.errors['password2'],
                         [u'Both passwords must be the same'])


class Test_Login_Form(TestCase):
    ''' Test the login form '''

    def test_a_valid_login_form(self):
        ''' Test that the login form returns valid with valid input '''

        form = CustomerLoginForm({'username': 'test', 'password': 'test', })
        self.assertTrue(form.is_valid())

    def test_an_invalid_login_form_with_no_username_input(self):
        ''' Test that the login form return invalid
        with no username inputted '''

        form = CustomerLoginForm({'username': '', 'password': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_login_form_with_no_password_input(self):
        ''' Test that the login form return invalid
        with no password inputted '''

        form = CustomerLoginForm({'username': 'test', 'password': '', })
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_username(self):
        ''' Test that the form error
        'This field is required' occurs
        when the username is missing '''

        form = CustomerLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_missing_password(self):
        ''' Test that the form error 'This field is
        required' occurs when the password is missing '''

        form = CustomerLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class Test_Edit_Profile_Form(TestCase):
    ''' test the edit profile form '''

    def test_Edit_Profile_Form(self):
        ''' Test that the Edit Profile Form returns
        valid when there is valid changes '''

        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        first_name='first',
                                        last_name='last')
        data = {'username': 'changed',
                'first_name': 'changed',
                'last_name': 'changed',
                'email': 'changed@change.ie'}
        form = EditProfileForm(data, instance=user)
        self.assertTrue(form.is_valid())

    def test_correct_message_for_no_username_input(self):
        ''' Test that the error message 'This field is required'
        occurs when there is no username inputted in the field '''

        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        data = {'username': ''}
        form = EditProfileForm(data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_no_email_input(self):
        ''' Test that the error message
        'This field is required'
        occurs when there is no email
        inputted in the field '''

        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        data = {'email': ''}
        form = EditProfileForm(data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])
