# Code Institute - Stream 3 Project 
#### by Sarah Barron

### Accounts App
#### For registering, login & loging out of customers, customer profile's and reset password functionality.
##### Technologies used:
###### HTML - hypertext markup language
###### CSS - cascading style sheets 
###### Python - Programming Language
###### Bootstrap - A framework for developing responsive, mobile 1st websites.
###### Django - python web framework
- Admin - admin panel for users
- Authentication - used for authentication of customers registering & logging in
- Messages - used for displaying messages to the customers
- Forms - User Creation form - used for the creation of a new customer
- User model - the model I stored new customers details into - email, username, first name & last name

###### libraries i needed to install
- django forms bootstrap library for styling of forms
- news & special offers - pillow needed for using images
- new & special offers - ckeditor

## Testing
### Authentication

#### Register
- I clicked the register link on the navigation bar
- I was redirected to the registration page.
- I inputted the details into the form and clicked the register button
- I was directed back to the home page & welcome message to say i was registered was displayed.
- The username was displayed in the navigation bar and the navigation bar changed (login and register removed) and logout added
- I checked the django admin panel and the newly registered member was stored.

#### Login
- I clicked the login link on the navigation bar
- I was redirected to the login page
- Firstly i entered wrong details into the login form and an error message appeared and i was not logged in.
- The second attempt i entered the correct login details into the login form
- I was redirected to the home page and a message displayed to say I was successfully logged in.
- The username was displayed in the navigation bar and the register & login links were removed and the logout link added

#### Logout
- When I was logged in I clicked the Logout link on the navigation bar
- I was redirected back to the home page and message to say i was logged out was displayed
- The navigation bar removed the username and the logout link and added back the login & register link.

### Buying products from the shop
#### poduct app , cart app, checkout app

##### Purchasing product(s) that were within stock levels

I completed the same test for the following situations

1. Purchase of 1 product: purchase 1 quantity of product 1
2. Purchase of multiple of 1 product: purchase 6 quantity of product 1
3. Purchase 1 of 2 products: purchase 1 quanity of product 1 and 1 quantity of product 2
4. Purchase multiple of multiple products: purchase 6 quantity of product 1 and 3 quantity of product 2

###### Product.html
- I inputted the quantity of the ammount stated above for each product and clicked add. The chart badge updated to the correct number of items in the cart
- I clicked the cart link to cart.html

###### cart.html
- All product(s), quantities and total were correct 
- I clicked the checkout button which linked to checkout.html

###### checkout.html
- All product(s), quantites and total were correctly displayed
- I entered valid customer details
- I entered valid credit card details 
- I pressed the Submit Payment button
- As expected I was redirected back to the home page, the message to say my payment was succesfull appeared and the cart was emptied.

###### django 
- I checked the products app to make sure the stock levels were reduced by the appropriate quantity which they were
- I checked the checkout app to make sure the order was recorded
-- Customer details were recorded correctly
-- Ordered product(s) and quantites were recorded correctly

###### stripe.com
- I checked my stripe.com account to make sure that each payment & the correct payment was received.

##### Adjust cart test

I did the following test for all of the following scenario's

1. Amend 1 product - Added 4 quantity of product 1 amended the quantity to 6 (add more to the cart)
2. Amend 1 product - Added 6 quantity of product 1 amended the quantity to 3 (subtract from the cart)
3. Amend 1 product - Added 3 quantity of product 1 amended the quantity to 0 (empty the cart)
4. Amend 2 products - Added 5 quantity of product 1 amended the quantity to 3 (subtract from the cart) and Added 2 quantity of product 2 amended the quantity to 4 (add to the cart) 
5. Amend 2 products - Added 4 quantity to product 1 amended the quantity to 1 (subtract from cart) and Added 6 quantity to product 2 amended the quantity to 0(remove product from cart)
6. Amend 2 products - Added 2 quantity to product 1 amended the quantity to 0 and added 5 quantity to product 2 and amended it to 0 (empty cart)

###### Product.html
- I inputted the quantity of ammount stated above for each product and clicked add. 
- The cart badge updated to the correct number of items in the cart
- I clicked the cart link to cart.html

###### cart.html
- All product(s), quantities and total were correct
- I amended the quantites to the amounts stated above.
- The cart badge updated accordingly 
- I clicked the checkout button which linked to checkout.html all details on checkout.html corresponded with the amendments.

#####  Test of add to cart when quantity requested exceeds the available stock.

I did the following test for all of the following scenario's

1. 1 Product exceeds stock value: 
- Product 1 - Stock value = 10, inputted quantity = 20 (exceeds stock value)
2. 1 Product with no stock:
- Product 1 - Stock value = 0, inputted quantity =2 (exceeds stock value)
3. 2 Products 1 exceeds stock levels:
- Product 1 - Stock value = 6, inputted quantity = 15 (exceeds stock value)
- Product 2 - Stock value = 10, inputted quantity = 5 (in stock)
4. 2 Products both exceed stock leveles:
- Product 1 - Stock value = 5, inputted quantity = 10 (exceeds stock value)
- Product 2 - Stock value = 10, inputted quantity = 100 (exceeds stock value)
5. 2 Products both have no stock
- Product 1 - Stock value = 0, inputted quantity =5
- Product 2 - Stock value = 0, inputted quantity = 10


###### Product.html
- I inputted the quantity ammount stated above for each product and clicked add.
- The appropriate message appeared stating the max amount that could be bought and that the cart has been amended to this amount
- The cart badge updated with the new quantity of the product available to buy
- I Clicked the cart link to cart.html

###### cart.html
- All product(s), updated quantities and total were correct.

#####  Test of checkout view when the stock levels changed after adding them to the cart

I did the following test for all of the following scenario's

Initial value for stock for both product 1 and product 2 was 100
1. 1 Product exceeds stock value: 
- Product 1 - inputted quantity = 20, stock changed to 10
2. 1 Product with no stock:
- Product 1 - inputted quantity =2, stock changed to 0
3. 2 Products 1 exceeds stock levels:
- Product 1 - inputted quantity = 15, stock changed to 5
- Product 2 - inputted quantity = 5, stock not changed
4. 2 Products both exceed stock leveles:
- Product 1 - inputted quantity = 10, stock changed to 9
- Product 2 - inputted quantity = 20, stock changed to 10
5. 2 Products both have no stock
- Product 1 - inputted quantity =5, stock changed to 0
- Product 2 - inputted quantity = 10, stock changed to 0


###### Product.html
- I inputted the quantity ammount stated above for each product
- I clicked the add button.
- Stock levels are 100 at this time so products are added successfully
- The cart badge updates with inputted products and quantities
- I Clicked the cart link to cart.html

###### cart.html
- All product(s), quantities and total were correct.
- I clicked on the checkout button to bring me to checkout.html

###### django admin panel
- I reduced the stock values to the values stated above

###### checkout.html
- All product(s), quantites and total were correct
- I entered valid information into both the customer details form and the credit card details form.
- I click submit
- As the stock levels have changed to below the quantity that I have in my cart I was directed back to the cart.html page

###### cart.html
- A message is shown here informing me that about the stock levels and the carts have been amended to the maximum available and asks the person to check their cart before they proceed to checkout.
-  The cart was amended with the maximum available in stock
-  The badge was amended to show the cart with the max available stock
-  I clicked the checkout button again

###### checkout.html
- All product(s), quantites and total were correctly displayed


### Problems encountered
- I committed my env.py which held my develpment envrionmet variables to GitHub. To solve the problem i deleted the env.py file from all my previous Git Commits and added the the env.py file to .gitignore for all future commits

```
git filter-branch --tree-filter 'rm env.py' HEAD
git push origin master --force
git for-each-ref --format='delete%(refname)'refs/original|git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
echo env.py >> .gitignore

```
- I committed my SECRET KEY to GitHub. to solve this problem I generated a new SECRET_KEY using a [SECRET KEY Generator](https://www.miniwebtool.com/django-secret-key-generator/) I then added this new SECRET KEY to the env.py file 
-I deleted the old SECRET KEY from the settings.py file and added the following code to the settings.py file to point the SECRET KEY to the environment variables.
``` SECRET_KEY = os.environ.get('SECRET_KEY')``` 

- Iterating a dictionary and trying to remove using .pop() method. 
- I tried to iterate through my cart and pop/remove any items that had a 0 quantity value. Everytime the for loop poped/removed a value i would get a runtime error dictionary changed size during iteration. When i read up on this i discovered that you can not change a dictionary size during iteration. I came across an article [QUORA Article](https://www.quora.com/Working-in-Python-how-can-I-delete-items-while-iterating-over-a-dictionary) and used there tip to change the dictionary to a list and then iterate and pop. This worked perfectly.

``` 
    for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
```

### References
- Thanks to [Dalibor Nasevic's article](https://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-git-repo) which helped me with the commands to remove all env.py files from my git commit history.
- I used the [CKEDITOR documentation](https://django-ckeditor.readthedocs.io/en/latest/) to give me a text editor and image uploader for my News & Special Offers content field.
- [QUORA Article](https://www.quora.com/Working-in-Python-how-can-I-delete-items-while-iterating-over-a-dictionary) This article helped me with the "RUNTIME ERROR dictionary changed size during iteration" I used their tip to change the dictionary to a list.
- [YouTube Video that helped with setting up editing user profile](https://www.youtube.com/watch?v=D9Xd6jribFU) 

[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)