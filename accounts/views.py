from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomerLoginForm, CustomerRegistrationForm, EditProfileForm
from checkout.models import OrderLineItem
from review.models import Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# REGISTRATION

# register a new customer
def register_customer(request):
    
    #if memeber is already logged in return to the index page
    if request.user.is_authenticated:
        messages.info(request, 
        'You are already logged in! If this is not you please <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/logout/">logout</a> and click register again', 
        extra_tags="safe")
        return redirect(reverse('index'))
    
    # if its a POST method
    if request.method=="POST":
        #pass the values that the new customer has inputted into the form
        registration_form = CustomerRegistrationForm(request.POST)
        
        #if the registration form is valid
        if registration_form.is_valid():
            # save the details taken from the registration form in the Database
            registration_form.save()
            # create the customer
            customer = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1'])
        
            #log the newly registered customer in
            if customer:
                auth.login(user=customer, request=request)
                messages.success(request, "Welcome you are now registered")
                return redirect(reverse('index'))
        
        # otherwise throw an error message to tell the person they can't register
        else:
            messages.error
            (request, 'Sorry but we are unable to register you at this time')
    
    # otherwise 
    else:
        # create an instance of a blank Customer Registration Form
        registration_form = CustomerRegistrationForm()

    #go to the registration.html page with the registration form
    return render(request, 'registration.html',
    {"registration_form": registration_form})
    

# LOGIN

# login an already registered customer 
def login_customer(request):
    
    # if a customer is already logged in they can't login again so 
    #return them the home page with a message you are already logged in
    if request.user.is_authenticated:
        
        messages.info(request, 
        'You are already logged in! If this is not you <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/logout/">logout</a> and log back in again under your own username', 
        extra_tags="safe")
        return redirect(reverse('index'))
        
        
    # if its a POST method
    if request.method=="POST":
        
        #pass in the values that the customer has inputted for username and password
        customer_login_form = CustomerLoginForm(request.POST)
        
        # check to see if the data in the customer login form is valid
        if customer_login_form.is_valid():
            customer = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
        
            #if the form is valid login the customer 
            if customer:
                auth.login(user=customer, request=request)
                messages.success(request, 'WELCOME You have successfully logged in!')
                
                # if the customer is required to login for checkout / reviews they will be redirected back to the checkout or review pages after login
                nexturl= request.POST.get('next')
                if nexturl:
                    return redirect(nexturl)
                #otherwise they will be redirected back to the index.html page
                else:
                    return redirect('index')
               
                
            #otherwise send a message to say the form is invalid
            else:
                customer_login_form.add_error(None, "Your username or password is incorrect, please try again!")
                
    #If there is no POST method return an empty instance of the customer login form
    else:
        #create an instance of the login form
        customer_login_form = CustomerLoginForm()
    
    # go to the login.html file and input a customer_login_form
    return render(request, 'login.html', {"customer_login_form": customer_login_form})
    

# LOGOUT 

# the logout_customer view can only be accessed if the customer is already logged in
# if they are not logged in they will be reverted to the login page
@login_required

# logout customer returns the index page
def logout_customer(request):
    #logout the customer
    auth.logout(request)
    
    # the logout message that the customer will see
    messages.success(request, 
    'You have logged out successfully.We hope to see you again soon! <a href="https://stream-3-project-sarahbarron.c9users.io/accounts/login/">login</a> again', 
    extra_tags="safe" )
    
    #return to the home page index.html
    return redirect(reverse('index'))


# CUSTOMER PROFILE

# you must be logged in to view your profiel
@login_required
def customer_profile(request):
    
    # PROFILE SECTION
    
    # an instance of the customer that is logged in
    profileuser = request.user
    
    # ORDERS SECTION
    
    # an instance of all orders made by customer logged in and order them by most recent date
    myorders = OrderLineItem.objects.filter(user = profileuser).order_by('-order')
   
    # paginator for myorders with 5 orders per page
    paginator = Paginator(myorders, 5) 
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, give the first page of results.
        orders = paginator.page(1)
    except EmptyPage:
        # If page is out of range give the last page of results.
        orders = paginator.page(paginator.num_pages)
    
    
    # REVIEWS SECTION
    
    # an instance of all reviews made by the customer logged in and order it by most recent date
    customer_review = Review.objects.filter(user = profileuser).order_by('-date')
    
    #paginator for reviews with 3 reviews per page
    review_paginator = Paginator(customer_review, 3) 
    review_page = request.GET.get('page')
    try:
        reviews = review_paginator.page(review_page)
    except PageNotAnInteger:
        # If page is not an integer, give the first page of results.
        reviews = review_paginator.page(1)
    except EmptyPage:
        # If page is out of range give the last page of results.
        reviews = review_paginator.page(review_paginator.num_pages)
    
    #this will return the user matching the email address stored in the request
    customer = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"customer_profile": customer, "orders": orders, "reviews": reviews})


# EDIT PROFILE

# you must be logged in to edit your profile
@login_required
def edit_profile(request):
    
    # if it is a post method
    if request.method == 'POST':
        
        #get an instance of the edit profile form
        form = EditProfileForm(request.POST, instance=request.user)
        
        # set someone_has_this initially to false
        someone_has_this= False
        
        
        # if the email field or the username field or both fields were changed do the following
       
        if "email" in form.changed_data or "username" in form.changed_data:
             
            # if the email field was changed do the following
            if "email" in form.changed_data:
                
                # the email input from the form
                form_email = request.POST['email']
                
                # a filter of all users with the same email address as what was posted in the form
                filter_emails= User.objects.filter(email = form_email)
                
                            
                # for all users with the same email address as what was posted in the form
                for filter_email in filter_emails:
                    
                    # if the email address is associated with another user id
                    if filter_email.id != request.user.id:
                        
                        # set someone_has_email to True
                        someone_has_this = True
                        
                        # display a message to say someone has this email address
                        messages.error(request, "Somebody with this email address is already registered please enter a unique email address" )
                        #return to the edit profile page
                        return redirect(reverse('edit_profile'))
            
            # if the username field has been changed do the following
            if "username" in form.changed_data:
                
                # the username input from the form
                form_username = request.POST['username']
                
                # a filter of all users with the same username as what was posted in the form
                filter_usernames = User.objects.filter(username = form_username)
                        
                # for all users with the same username as what was posted in the form 
                for filter_username in filter_usernames:
                    
                    # if the username is associated with another user id
                    if filter_username.id != request.user.id:
                        
                        # set someone has this to True
                        someone_has_this = True
                        
                        # otherwise display a message to say someone has this username
                        messages.error(request, "Somebody already has this username please enter a unique username" )
                        #return to the edit profile page
                        return redirect(reverse('edit_profile'))
    
    
        # if the form is valid and nobody has the same email address or username save the form and redirect back to the customer profile
        if form.is_valid() and someone_has_this==False:
            form.save()
            return redirect('customer_profile')
    
    # otherwise return an empty instance of the edit profile form    
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'editprofile.html', {'form': form})
   
    