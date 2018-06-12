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
- pillow needed for using images

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


[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)