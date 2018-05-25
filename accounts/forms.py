from django import forms

# The form for customer to login 
class CustomerLoginForm(forms.Form):
    
    #text input box for the customers chosen username
    username = forms.CharField()
    
    #text input box of type password for the customers chosen password
    password = forms.CharField(widget=forms.PasswordInput)