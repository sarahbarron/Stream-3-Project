# Code Institute - Stream 3 Project 
#### by Sarah Barron

## Testing
## Django Test Suite
##### I used the Django Test Suite to test all my apps and used Coverage to generate a report in which I initally scored 83% and after adding extra tests i finished with 119 tests and a score of 99% tested. Which covered 1598 statements and missing 12. All tests can be viewed within each app folder

- Accounts App: tests\_app.py, tests\_forms.py, tests\_models.py, and tests\_views.py 
- Cart App: tests\_app.py, and tests\_views.py
- Checkout App: tests\_app.py, tests\_forms.py, tests\_models.py, and tests\_views.py 
- Posts App: tests\_apps.py, tests\_forms.py, tests\_models.py, and tests\_views.py 
- Products App: tests\_apps.py, tests\_models.py, and tests\_views.py 
- Productsearch App: tests\_apps.py and tests\_views.py
- Review App: tests\_apps.py, tests\_forms.py, test\_models.py, and tests\_views.py 
- Home App: tests\_app.py, test\_views.py 


![Django Testing](/static/img/DjangoTestingScore.JPG)

## Manual Testing
### Users & Authentications - accounts app

#### Manual testing registering 
##### test 1: registering a new customer
- I clicked the register link on the navigation bar
- I was redirected to the registration page.
- Initially i ommitted some details and put a wrongly formated email address in the email field and the form validation all worked as it should have
- I then inputted the details correctly into the form and clicked the register button
- I was directed back to the home page & welcome message to say i was registered was displayed.
- The username was displayed in the navigation bar and the navigation bar changed (login and register removed) and logout was now visable
- I checked the django admin panel and the newly registered member was stored.

##### test 2: trying to register a customer who is already logged in
- I logged in as an already registered user.
- I entered the [register link](https://stream-3-project-sarahbarron.c9users.io/accounts/register/)
- I was redirected to the home page and a message to tell me i was already logged in appeared.

#### Manual testing login
##### test 1: login an already registered customer
- I clicked the login link on the navigation bar
- I was redirected to the login page
- Firstly i entered wrong details into the login form and an error message appeared and i was not logged in.
- The second attempt i entered the correct login details into the login form
- I was redirected to the home page and a message displayed to say I was successfully logged in.
- The username was displayed in the navigation bar and the register & login links were removed and the logout link added

##### test 2: trying to login when already logged in
- I logged in as an already registered user.
- I entered the [login link](https://stream-3-project-sarahbarron.c9users.io/accounts/login/)
- I was redirected to the home page and a message to tell me i was already logged in appeared.

#### Manual testing logout
##### test 1: logout a customer 
- When I was logged in I clicked the Logout link on the navigation bar
- I was redirected back to the home page and message to say i was logged out was displayed
- The navigation bar removed the username and the logout link and now showed the login & register link.

##### test 2: entering the logout link when no-one was logged in 
- I made sure no-one was logged in.
- I entered the [logout link](https://stream-3-project-sarahbarron.c9users.io/accounts/logout/)
- I was redirected to the login page as you must be logged in in order to logout.

#### Manual testing: Viewing a Profile
- I logged in
- Clicked on the Profile / Track Order link on the navigation bar
- This brought me the the profile page which showed me my profile details, my past order details and my reviews.
- the orders were paginated 
- the reviews were paginated

#### Reset Password
- Clicked the forgotten password link
- This directed me to the password reset page where i inputted my email address and clicked the reset password button
- This directed me to the password reset done page informing me that an email had been sent to my email address
- I checked my email and the email was there with a link to reset the password.
- I followed the link and was directed to the password reset confirm page where i entered my new password twice and clicked the reset password button
- This brought me to the password reset complete page with a link to login with my new password.

#### Manual testing edit profile (note during my first test i found a problem outlined in problems encountered below) this test was redone when problems were fixed
##### test 1: changing data with a unique username, email address and first name and lastname 
- clicked on the edit profile link
- This directed me to the profileform page where i could change my username, email address, first name or last name. I could also click a link to reset my password.
- I changed my username, email address, first name and last name and pressed save.
- I checked the admin panel and could see the changes made there 

##### test 2: changing data with the same email address as another user
- I clicked on the edit profile link
- This directed me to the profile form 
- I changed my email address to the same email address as another user and pressed the save button
- I was redirected to the profileform page with a message to say another user has that email address and to use a unique email address
- I checked the admin panel and no changes had been made

##### test 3: changing data with the same username as another user
- I clicked on the edit profile link
- This brought me to the profile form 
- I changed my username to the same username as another user
- I was returned to the profile form with a message to say another user has that username and to use a unique username
- I checked the admin panel and no changes had been made

##### test 4: changing data with the same username as another user and the same email address as another user
- clicked on the edit profile link
- This brought me to the profile form 
- I changed my username to the same username as another user and email address to the same email address as another user
- I was returned to the profile form with a message to say Somebody with this email address is already registered please enter a unique email address
- I checked the admin panel and no changes had been made

### Posts - posts app
#### Create a posts
##### test 1: create a post logged in as a staff member
- I logged in as a staff member
- Clicked the New Post link on the navigation bar.
- This brings you to blogpostform.html with the form to input your post
- I inputted the details
- Pressed the save button
- Checked the posts database and the new post was saved

##### test 2: try to create a post logged in as a user without staff status
- I logged in as a user without staff status
- entered the [new post link](https://stream-3-project-sarahbarron.c9users.io/posts/new/)
- I was redirected to the home page and the message "You are not authorised to create or edit posts" was displayed

##### test 3: try to create a post when not logged in
- I entered the [new post link](https://stream-3-project-sarahbarron.c9users.io/posts/new/)
-  I was redirected to the login page.
-  The first time I logged in as a staff member user and was redirected to the create post page
-  The second time i logged in as a user with no staff status and i was redirected to the home page with a message welcome you are not authorised to create or edit posts displayed

#### view all posts (did the same test below with a user logged in and with no user logged in)
- clicked on the News & Special Offers link on the navigation bar
- This brought me to the allposts.html page and showed all posts from the posts database.

#### View a post in full (did the same test below for a user logged in and with no user logged in)
- I clicked on the Read More button on the post I wanted to see in full
- This brought me to the fullpost page showing the expected post in full.

#### Edit Posts 
##### test 1: edit a post logged in as a staff member
- I logged in as a staff member.
- Clicked the Edit Post button.
- This brings you to blogpostform.html with the form and the posts information filled into the form.
- I changed some details
- Pressed the save button
- checked the posts database and the changes had been saved

##### test 2: try to edit a post logged in as a user without staff status
- I logged in as a user without staff status
- I entered the [edit post link](https://stream-3-project-sarahbarron.c9users.io/posts/6/edit/)
- I was redirected to the home page and the message "You are not authorised to create or edit posts" was displayed

##### test 3: try to edit a post when not logged in
- I entered the [edit post link ](https://stream-3-project-sarahbarron.c9users.io/posts/6/edit/)
-  I was redirected to the login page.
-  The first time I logged in as a staff memeber user and i was redirected to the edit post page where I was able to edit the post
-  The second time I logged in as a user with no staff status and i was redirected to the home page with a message welcome you are not authorised to create or edit posts was displayed


#### delete posts
##### test 1: delete a post logged in as a staff member
- I logged in as a staff member.
- Clicked the Delete Post button.
- This brings you to allposts.html page and a message "your post was deleted" was displayed
- I checked the posts database and the post had been removed

#### test 2: delete a post logged in without staff status
- I logged in as a user without staff status
- entered the [delete post link](https://stream-3-project-sarahbarron.c9users.io/posts/8/delete)
- I was redirected to the home page with the message "You are not authorised to delete posts" displayed

#### test 3: delete a post not logged in 
- I logged out 
- entered the [delete post link](https://stream-3-project-sarahbarron.c9users.io/posts/8/delete)
- I was redirected to the login form.
- The first time I logged in as a user who did not have staff status. I was redirected to the home page and a message saying welcome you are not authorised to delete posts was displayed.
- I checked the database and the post had not been deleted
- The second time I logged in as a user with staff status. I was redirected to the the the allposts html page and a message to say the post was deleted appeared.
- I checked the database and the post was deleted.


### Buying products from the shop - poduct app , cart app, checkout app

#### Purchasing product(s) that were within stock levels

I completed the same test for the following situations

1. Purchase 1 quantity of 1 product 
2. Purchase 6 quantity of 1 product
3. Purchase 1 quanity of product 1 and 1 quantity of product 2
4. Purchase 6 quantity of product 1 and 3 quantity of product 2

##### Product.html
- I inputted the quantity of the ammount stated above for each product and clicked add. The chart badge updated to the correct number of items in the cart
- I clicked the cart link to cart.html

##### cart.html
- All product(s), quantities and total were correct 
- I clicked the checkout button which linked to checkout.html

##### checkout.html
- All product(s), quantites and total were correctly displayed
- First time I enter invalid customer details and errors as expected were shown to for required fields. 
- I then entered valid customer details
- First time I enter invalid credit card details and the expected error messages are shown
- I then entered valid credit card details 
- I pressed the Submit Payment button
- As expected I was redirected back to the home page, the message to say my payment was succesfull appeared and the cart was emptied.
- I checked my email and an email to tell me my order had been received was in my inbox with a link to my profile.
- I click on this link and I am brought to my profile page which shows my order status.

##### django 
- I checked the products app to make sure the stock levels were reduced by the appropriate quantity which they were
- I checked the checkout app to make sure the order was recorded
-- Customer details were recorded correctly
-- Ordered product(s) and quantites were recorded correctly

##### stripe.com
- I checked my stripe.com account to make sure that each payment & the correct payment was received.

#### Adjust cart test

I did the following test for all of the following scenario's

1. Added 4 quantity of product 1 amended the quantity to 6 (add more to the cart)
2. Added 6 quantity of product 1 amended the quantity to 3 (subtract from the cart)
3. Added 3 quantity of product 1 amended the quantity to 0 (empty the cart)
4. Added 5 quantity of product 1 amended the quantity to 3 (subtract from the cart) and Added 2 quantity of product 2 amended the quantity to 4 (add to the cart) 
5. Added 4 quantity to product 1 amended the quantity to 1 (subtract from cart) and Added 6 quantity to product 2 amended the quantity to 0(remove product from cart)
6. Added 2 quantity to product 1 amended the quantity to 0 and added 5 quantity to product 2 and amended it to 0 (empty cart)

##### Product.html
- I inputted the quantity of ammount stated above for each product and clicked add. 
- The cart badge updated to the correct number of items in the cart
- I clicked the cart link to cart.html

##### cart.html
- All product(s), quantities and total were correct
- I amended the quantites to the amounts stated above.
- The cart badge updated accordingly 
- I clicked the checkout button which linked to checkout.html all details on checkout.html corresponded with the amendments.

####  Test of add to cart when quantity requested exceeds the available stock.

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


##### Product.html
- I inputted the quantity ammount stated above for each product and clicked add.
- The appropriate message appeared stating the max amount that could be bought and that the cart has been amended to this amount
- The cart badge updated with the new quantity of the product available to buy
- I Clicked the cart link to cart.html

##### cart.html
- All product(s), updated quantities and total were correct.

####  Test of checkout view when the stock levels changed after adding them to the cart

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


##### Product.html
- I inputted the quantity ammount stated above for each product
- I clicked the add button.
- Stock levels are 100 at this time so products are added successfully
- The cart badge updates with inputted products and quantities
- I Clicked the cart link to cart.html

##### cart.html
- All product(s), quantities and total were correct.
- I clicked on the checkout button to bring me to checkout.html

##### django admin panel
- I reduced the stock values to the values stated above

##### checkout.html
- All product(s), quantites and total were correct
- I entered valid information into both the customer details form and the credit card details form.
- I click submit
- As the stock levels have changed to below the quantity that I have in my cart I was directed back to the cart.html page

##### cart.html
- A message is shown here informing me that about the stock levels and the carts have been amended to the maximum available and asks the person to check their cart before they proceed to checkout.
-  The cart was amended with the maximum available in stock
-  The badge was amended to show the cart with the max available stock
-  I clicked the checkout button again

##### checkout.html
- All product(s), quantites and total were correctly displayed

### Product Reviews - review app
#### create a review
##### test 1: try to write a review when logged in
- I clicked on the write a review link for a product
- this redirected me to reviewform.html page with a form to enter a review
- I inputted my review and pressed the save button
- I was then redirected back to the products page
- I checked the review database and the review had been stored correctly.

##### test 2: try to write a review when not logged in
- I clicked on the write a review link for a product
- I was directed to the login page
- When I logged in i was directed to the reviewform.html page with a blank form

#### Edit a review
##### test 1: edit a review logged in as the user who wrote the review
- I clicked the edit review button
- This brought me to the edit review page with the form and the review filled in
- I changed some things in the review and pressed save 
- I was redirected back to the profile page.
- I checked the review database and the changes had been saved in the review.

##### test :2 try to edit a review logged in as a different user to the user who wrote the review
- I logged in as a different user to the review writer
- I entered the [edit review link](https://stream-3-project-sarahbarron.c9users.io/reviews/edit/42/)
- I was redirected to the home page and the message "you are not authorised to edit this review" was shown

##### test 3: try to edit a review when logged out
- I logged out
- Entered the [edit review link](https://stream-3-project-sarahbarron.c9users.io/reviews/edit/42/)
- I was redirected to the login page
- when i logged in as the user who wrote the review i was directed to the reviewform page with the review populating the form ready for editing
- I repeated the test and logged in as a user who had not wrote the review and i was redirected to the home page and a message saying welcome you are not authorised to edit this review 

#### Delete review
##### test 1: delete a review logged in as the user who wrote the review
- I logged in
- I clicked the delete review button
- I was redirected back to the profile page and a message to say the review has been deleted was shown
- I checked the review database and the review was gone.

##### test 2: try to delete a review logged in as a different user to the user that wrote the review
- I logged in as a different user to the user who wrote the review
- I entered the [delete review link](https://stream-3-project-sarahbarron.c9users.io/reviews/delete/37/)
- I was directed back to the home page and a message to say you are not authorised to delete this review
- I checked the review database and the review was still there

##### test 3: try to delete a review while logged out
- I logged out
- I entered the [delete review link](https://stream-3-project-sarahbarron.c9users.io/reviews/delete/37/)
- I was directed to the login page
- The first time I logged in as a user who did not write the review - i was directed to the home page and a message saying welcome you are not authorised to delete this post.
- I checked the review database and the review was still there
- The second time I logged in as the user who wrote the review and I was directed to the profile page and a message to say the review has been deleted was shown
- I checked the review database and the review had been removed

#### View all reviews for a product (tested both while logged in and with no user logged in)
- Go to the products page (the shop link on the navigation bar)
- I clicked on the view reviews link for a product
- This brought me to the allreviews.html page which showed all reviews from the reviews datatbase only for that product as expected

#### View a review in full (tested both while logged in and with no user logged in)
- I clicked on the Read More button on the review I wanted to see the full review
- This brought me to the fullreview html page showing the expected review in full.

## Cross Browser Testing 
#### Chrome 
- I used chrome as my main browser when doing my project

#### Firefox 
- The filp effect on the treatments in the index.html page did not work as expected in firefox. When hovering over the treatment the back div became visble and the front remained visible. Also the link at the the end of the back div did not act as a link.
- I fixed this problem by adding the following code to the mousein class 
``` 
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    -o-backface-visibility: hidden;
    -ms-backface-visibility: hidden;
```

#### Microsoft Edge
- Only a small change was need here a horizontal rule was showing incorrectly in the contact section on the index.html page
- I fixed this problem by removing the following code from the #contact hr
```
text-align:center
```

#### Internet explorer
- During testing I discovered my flip card effect on the index.html and the products.html page did not work. When hovered on the front div the back div did not become visible after some research i found that backface-visibility was only partially supported by IE as it does not support the transform-style: preserve-3d property.
- To solve this problem I changed my javascript to detect if the website was being viewed on an Internet explorer browser and if it was I did added no class and left the front div static, which removed the 3d flip effect. Users could use the relevent link to go to the treatments.html page or to the product description page to learn more.

#### Opera 
- No problems detected 

## Mobile/Tablet responsive testing
- I used Developers Tools to test responsiveness. Using this method I was able to test my project on the following devices:
-- Blackberry Z30, Blackberry playbook, Galaxy Note 3, Galaxy Note II, Galaxy S III, Kindle Fire HDX, LG Optimus L70, Laptop with HiDPI screen, Laptop with MDPI screen, Laptop with touch, Microsoft Lumia 550, Microsoft Lumia 950, Nexus 10, Nexus 4, Nexus 5, Nexus 5X, Nexus 6, Nexus 6P, Nexus 7, Nokia Lumia 520, Nokia N9, iPad Mini, iPhone 4, Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro

## HTML Validation
- I validated all of my HTML pages using the [W3 Html Validator](https://validator.w3.org/). I fixed all issues that i could. However there are still some issues arising from the CKEDITOR.

## CSS Validatation
- I validated my css file with the [W3 CSS validator](https://jigsaw.w3.org/css-validator/)
- .

## JavaScript Validation
- I validated my Javascript files with [JShint](http://jshint.com/).