# Code Institute - Stream 3 Project 
#### by Sarah Barron

## What my project does and the needs it fulfils
- This project is a business website. It was built for a client running a beauty salon. The website is needed for e-commerce, advertising and providing all the necessary information about the beauty salon, it provides details about treatments and price, news and special offers, contact and location. It also provides an online store for buying beauty products.
- The website has a customer registration. This is currently needed for purchasing prodcuts online and writing customer reviews. The customer has a profile area where they can track the status of an order and view all past orders. It also contains all reviews made by the customer and they can edit or delete these reviews as they wish. Along with that the customer can also amend and update their username or email address. 

## Technologies used:

##### HTML - hypertext markup language
##### CSS - cascading style sheets 
##### Javascript - client side scripting language
##### Python - Programming Language
##### Git Bash & GitHub -for version control and backup of code
##### Bootstrap - A framework for developing responsive, mobile first websites.
##### Django - python web framework
##### Libraries i needed to install
- django forms bootstrap library for styling of forms
- pillow needed for using images
- ckeditor for rich text editing in creating and editing posts 

##### Plugin - Coverage - I needed this during my testing of code. It generates reports which show you how much of your code you have tested.
##### Stripe - needed for online payment transactions for purchasing products
##### EmailJs - needed for the contact format
##### Gmail - needed for emails
##### Tiny Png - Used to optimise all photos used in the project [https://tinypng.com/](https://tinypng.com/) 

## Testing

- I have outlined my testing in a seperate file  [testing.md - click here to view it](https://github.com/sarahbarron/Stream-3-Project/blob/master/testing.md)

## Problems encountered

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