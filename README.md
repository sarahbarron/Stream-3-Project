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
- I committed my env.py file to GitHub. To solve the problem i deleted the env.py file from all Git Commits History using 

''' 
git filter-branch --tree-filter 'rm env.py' HEAD
git push origin master --force
git for-each-ref --format='delete%(refname)'refs/original|git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now

'''
- I then added my env.py file to my .gitignore file for all future commits

- I committed my SECRET KEY to GitHub. to solve this problem. I generated a new SECRET_KEY using a [SECRET KEY Generator](https://www.miniwebtool.com/django-secret-key-generator/) I added this new SECRET KEY to the env.py file and ammended the settings.py file to point to the env.py file to find the newly generated SECRET KEY.  


[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)