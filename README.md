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

#### Testing
###### Chart
###### Checkout
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

``` for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
```

### References
- Thanks to [Dalibor Nasevic's article](https://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-git-repo) which helped me with the commands to remove all env.py files from my git commit history.
- I used the [CKEDITOR documentation](https://django-ckeditor.readthedocs.io/en/latest/) to give me a text editor and image uploader for my News & Special Offers content field.
- This article helped me with runtime error dictionary changed size during iteration is was getting while trying to iterate and remove items from a dictionary [QUORA Article](https://www.quora.com/Working-in-Python-how-can-I-delete-items-while-iterating-over-a-dictionary)


[![Build Status](https://travis-ci.org/sarahbarron/Stream-3-Project.svg?branch=master)](https://travis-ci.org/sarahbarron/Stream-3-Project)