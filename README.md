[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)
# Code Institute - Stream 3 Project 
### By Sarah Barron

## About this project

##### I am currently a student at the Code Institute doing a Full Stack Diploma in Software Development. This is the third of three projects which I must complete in order to be awarded the globally recognised Diploma from Edinburgh Napier University. This project will cover the Full Stack i.e all sections of the course both frontend and backend web development.

##### This project is based on a Beauty Salon.

## The needs this project fulfils

- This is a business website. It is built for a client running a beauty salon. The website is needed for e-commerce to sell beauty products, advertising and providing all the necessary information about the beauty salon. It provides details about treatments and prices, news and special offers, contact and location.

## What my project does

- Anyone who visits this website can view 
    - The landing page which has information about
        - Treatments - A synopsis of the treatments being offered at the salon.
        - Shop - A synopsis about Tomitago the product that is being sold.. 
        - News and Special Offers synopsis - this shows the first few lines of the current news and specials that have been choosen to be viewed on the landing page.
        - Contact details - Name, address, telephone, email, a link to facebook, a contact form and location on google maps. This can be linked to from the navigation bar and at the bottom of the treatments page.
    - The treatments page which can be accessed from the navigation bar and the landing page. This shows a list of all treatments being offered and the prices.
    - The Shop - there is a link to this page from the navigation bar and landing page. This shows all products being sold online. From this page all users can: 
        - Add products to the cart.
        - View reviews about a product.
    - News and Special Offers - this is a blog page that can be accessed from the navigation bar or the landing page. It shows a synopsis of all news and special offers . From this page all users  can click on the read more button to bring them to the full post page.
    - The product search input box - located in the footer. This can be used to search for a certain product in the shop.

- Anyone who visits the page has the option to
    - login or
    - Register

The login and register pages can be accessed from the navigaion bar

- Logged in users have some extra features they can access
    - On the shop page they can write a review about any product.
    - View the cart page - to view all items that have been added to the cart during the session. The quantity required of each product can also be amended on this page. The cart is accessable from the cart link on the navigation bar.
    - Checkout - to purchase the items in the cart. The link to the checkout is accessable from the cart page.
    - Profile - Every registered user has a profile. Once a user is logged in the link to the profile page will be  shown on the navigation bar. There is 3 sections to the profile
        1. The users information - Name, Username & Email address the user has the option to edit this information using the the edit button in this section
        2. The users past orders - If the user has purchased any products online this information will be stored here and the delivery status will be shown. There is a paginator in this section that shows 5 orders per page.
        3. The users past reviews - If the user has made a review on a product the review will be shown here. The user has the option to edit or delete the review from here. There is a paginator in this section that only shows 3 reviews per page.
    - Logout - the logout link is on the navigation bar.

- Staff members have all the same features as a logged in user plus some extra features.
    - Add a post - The link to add a post is on the navigation bar. This allows the staff member easily add news and special offer posts.
    - On the news and specials page the staff member can easily edit or delete a post. This can also be done when viewing the post in full.
    - Access to the admin panel where the staff member can manage users, products, posts, checkout orders and reviews.

## Technologies used:

##### Cloud9 - cloud based IDE to create the project
##### Heroku - to deploy the project
##### AWS - Amazon Web Services
- AWS S3 - to store static and media files and to serve the website
- AWS IAM - manages user access and encryption keys

##### Travis CI - Used to build and test the project
##### HTML - hypertext markup language
##### CSS - cascading style sheets 
##### Javascript - client side scripting language
##### Python - Programming Language
##### Git Bash & GitHub -for version control and backup of code
##### Bootstrap - A framework for developing responsive, mobile first websites.
##### Django - python web framework
##### Libraries and packages i needed to install

- django forms bootstrap library for styling of forms
- pillow needed for using images
- ckeditor for rich text editing in creating and editing posts
- dj-database-url to allow connection to database url
- psycopg2 to allow connection to postgress database
- django storages and botoS3- both needed to use django with S3
- gunicorn - to connect to heroku
- pycodestyle - to check the style of the python code is correct and show any styling errors

##### Plugin - Coverage - I needed this during my testing of code. It generates reports which show you how much of your code you have tested.
##### Stripe - needed for online payment transactions for purchasing products
##### EmailJs - needed for the contact forms
##### Gmail - needed for emails
##### Tiny Png - Used to optimise all photos used in the project [https://tinypng.com/](https://tinypng.com/) 

## Testing

- I have outlined my testing in a seperate file  [testing.md - click here to view it](https://github.com/sarahbarron/Stream-3-Project/blob/master/testing.md)

## Deployment

- Set up an [heroku app](https://dashboard.heroku.com/apps)
- Added on the Heroku Postgress Database
- Installed the package dj-database-url to allow connection to a database url
- Installed the package psycopg2 for connecting to postgress databases
- Setup the default database in settings.py to the postgres database
- Migrated the project in order to use the new postgres datatbase
- Created a superuser
- Set up a AWS S3 bucket to serve the website
- Set up an AWS IAM - to manage user access and encrytion 
   - Setup a group 
   - Created a policy
   - Attached the group to the policy
   - Created a user
   - Downloaded the users keys .csv file
- Installed django-storages  and botoS3 in order to use dajango with S3
- Setup Django to connect with AWS
- Setup Travis CI to build and test the project
- Setup my config variables in Heroku
- Installed the package gunicorn to connect my project to Heroku. 
- Disabled collectstatic in heroku so heroku wont try to upload the static files.
- Deployed the project on heroku
- Added the heroku address to valid hosts in settings.py
- You can view the deployed website [here](https://ginas-beauty-studio.herokuapp.com/)

## Problems encountered throughout the project

- I committed my env.py which held my private develpment envrionmet variables to GitHub. To solve the problem i deleted the env.py file from all my previous Git Commits and added the the env.py file to .gitignore for all future commits

```
git filter-branch --tree-filter 'rm env.py' HEAD
git push origin master --force
git for-each-ref --format='delete%(refname)'refs/original|git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
echo env.py >> .gitignore

```

- I committed my SECRET KEY to GitHub. to solve this problem I generated a new SECRET_KEY using a [SECRET KEY Generator](https://www.miniwebtool.com/django-secret-key-generator/) I then added this new SECRET KEY to the env.py file 
-I deleted the old SECRET KEY from the settings.py file and added the following code to the settings.py file to point to the new SECRET KEY in the env.py file.

``` SECRET_KEY = os.environ.get('SECRET_KEY')``` 

- Iterating a dictionary and trying to remove using .pop() method. I tried to iterate through my cart and pop/remove any items that had a 0 quantity value. Everytime the for loop poped/removed a value i would get a runtime error dictionary changed size during iteration. When i read up on this i discovered that you can not change a dictionary size during iteration. I came across an article [QUORA Article](https://www.quora.com/Working-in-Python-how-can-I-delete-items-while-iterating-over-a-dictionary) and used there tip to change the dictionary to a list and then iterate and pop. This worked perfectly.

``` 
    for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
```

- The edit_profile view. When manually testing the view I discovered that you could change the username and email address to the same username or email address of other users. I had to add extra python code to the view to check that other users did not have the same username or email address as what the user wanted to change to.

- When testing my checkout views.py. I could not test with my STRIPE\_PUBLISHABLE key. It would return an error. After researching the Stripe documentation i came across the [test card numbers and tokens](https://stripe.com/docs/testing#cards). The token I needed for the card number i was using was tok\_visa

## References

- [Django Documentation](https://docs.djangoproject.com/en/2.0/) helped me with all backend aspects of my project. 
- Thanks to [Dalibor Nasevic's article](https://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-git-repo) which helped me with the commands to remove all env.py files from my git commit history.
- I used the [CKEDITOR documentation](https://django-ckeditor.readthedocs.io/en/latest/) to give me a text editor and image uploader for my News & Special Offers content field.
- [QUORA Article](https://www.quora.com/Working-in-Python-how-can-I-delete-items-while-iterating-over-a-dictionary) This article helped me with the "RUNTIME ERROR dictionary changed size during iteration" I used their tip to change the dictionary to a list.
- Max Goodridge's [YouTube Video](https://www.youtube.com/watch?v=D9Xd6jribFU) helped put me in the right direction with setting up editing the user profile by talking about the UserChangeForm.
- [Stripe Documentation](https://stripe.com/docs) - helped me with my stripe payments and testing

[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)

## Thank You

I would like to thank the [Code Institute](https://www.codeinstitute.net/) and [Springboard](https://springboardcourses.ie/) for providing me with such a wonderful course and experience. I have enjoyed every minute learning and practicing all that I have learnt. A massive thank you must go to my Mentor Yoni Lavi who helped me so much along the way and to my tutors Nakita McCool and Neil McEwel for being so quick to respond and help when issues arose. Also, thanks to Tiffany Snell for your constant communication and response to any problems I had. To my fellow students on Slack, I really appreciate all the advice, help and for just keeping me company while I studied remotely, I would have been lost without you, so Thank You.