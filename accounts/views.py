from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import CustomerLoginForm


# logout customer returns the index page
def logout_customer(request):
    #logout the customer
    auth.logout(request)
    
    # the logout message that the customer will see
    messages.success(request, "You have logged out successfully. We hope to see you again soon!")
    
    #return to the home page index.html
    return redirect(reverse('get_index'))

# login an already registered customer 
def login_customer(request):
    
    # if its a POST method
    if request.method=="POST":
        
        #pass the details that the customer has inputted into for username and password
        customer_login_form = CustomerLoginForm(request.POST)
        
        # check to see if the data in the customer login form is valid
        if customer_login_form.is_valid():
            customer = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
        
            #if the form is valid
            if customer:
                auth.login(user=customer, request=request)
                messages.success(request, 'You have successfully logged in. Welcome back!')
                
            #otherwise send a message to say the form is invalid
            else:
                customer_login_form.add_error(None, "Your username or password is incorrect, please try again!")
                
    #If there is no POST method return an empty instance of the customer login form
    else:
        #create an instance of the login form
        customer_login_form = CustomerLoginForm()
    
    # go to the login.html file and input a customer_login_form
    return render(request, 'login.html', {"customer_login_form": customer_login_form})
    
    
    


# def register_customer(request):



# def customer_profile(request):

