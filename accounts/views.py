from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import CustomerLoginForm


# logout customer returns the index page
def logout_customer(request):
    #logout the user
    auth.logout(request)
    #message that the Customer will see
    messages.success(request, "You have logged out successfully. We hope to see you again soon!")
    return redirect(reverse('get_index'))

# login an already registered customer 
def login_customer(request):
    
    # if it = POST create an instance of the Customer login form and pass in the
    # details that the customer has inputted into the form
    if request.method=="POST":
        customer_login_form = CustomerLoginForm(request.POST)
        
        # check to see if the data in the customer login form is valid
        if customer_login_form.is_valid():
            customer = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
        
            #if the form is valid
            if customer:
                auth.login(user=customer, request=request)
                messages.success(request, 'Your have successfully logged in. Welcome back!')
                
            #otherwise send a message to say the form is invalid
            else:
                customer_login_form.add_error(None, "Your username or password is incorrect, please try again!")
                
    #otherwise return an empty instance of the customer login form
    
    else:
        #create an instance of the login form
        customer_login_form = CustomerLoginForm()
    
    
    return render(request, 'login.html', {"customer_login_form": customer_login_form})

        
    
    


# def register_customer(request):



# def customer_profile(request):

