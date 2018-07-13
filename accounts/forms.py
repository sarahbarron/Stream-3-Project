from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

# CUSTOMER REGISTRATION FORM
class CustomerRegistrationForm(UserCreationForm):
    #this form inherits from Djangos already created User Creation Form
    
    #password fields
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Re-enter your password', 
        widget=forms.PasswordInput)
    
    # an inner class to provide information about the form (known as Meta classes in Django) 
    class Meta:
        # the model we want to store the information in which is the User model
        model = User
        #the fields we want in our form
        fields = ['email', 'username', 'password1', 'password2','first_name', 'last_name']
    
    #email validation
    def clean_email(self):
        #clean the email & username field & return them once cleaned
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        #check the database to see if the email address is already there
        # if the email is already in the database raise an error message
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('Somebody with this email address is already registered')
        # if the email address is not in the database return the email address
        return email
    
    def clean_password2(self):
        #clean password 1 and password 2 return them once cleaned
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # if either password1 or password2 are blank throw the following error
        if not password1 or not password2:
            raise ValidationError('Please enter matching passwords')
        
        # if password1 and password2 are not the same throw the followng error
        if password1 != password2:
            raise ValidationError('Both passwords must be the same')
        
        # otherwise return password2
        return password2
        
# CUSTOMER LOGIN FORM
class CustomerLoginForm(forms.Form):
    
    #text input box for the customers chosen username
    username = forms.CharField()
    
    #text input box of type password for the customers chosen password
    password = forms.CharField(widget=forms.PasswordInput)


# Edit Customer Profile
class EditProfileForm(UserChangeForm):
     # an inner class to provide information about the form (known as Meta classes in Django) 
    class Meta:
        # the model we want to store the information in which is the User model
        model = User
        # the fields we want to be able to edit
        fields = ['email', 'username','first_name', 'last_name', 'password']
        
    
    