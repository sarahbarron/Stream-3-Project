from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product 
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages

'''
REVIEW VIEWS
'''

# you must be logged in to create a review
@login_required()
def new_review(request, id, pk=None):

    # the product being reviewed
    product = get_object_or_404(Product, pk=id)
    
    # get an instance of Review 
    review = get_object_or_404(Review, pk=pk) if pk else None
    
    # if the method is post
    if request.method == "POST":
        
        # get a ReviewForm instance
        form = ReviewForm(request.POST, request.FILES, instance=review)
        
        #  if the form is valid
        if form.is_valid():
            
            # save the form input
            review = form.save()
            
            # assign the review product as the product being reviewed
            review.product = product
            
            # assing the review user as the logged in user
            review.user = request.user
            
            # get the review rating
            review_rating = review.rating
            
            # get the number of reviews 
            num_of_ratings = product.num_of_ratings
            
            # increment the number of reviews by 1
            new_num_of_ratings = num_of_ratings + 1
            
            # get the average review rating
            average = product.average_rating
            
            # calculate the new average review rating
            average = average + ((review_rating - average) / new_num_of_ratings)
            
            # assign the products number_of_ratings to the new number of ratings value   
            product.num_of_ratings = new_num_of_ratings
            
            # assign the products average rating to the newly calculated rating  
            product.average_rating = average
            
            # save the review    
            review.save()
            
            # save the product
            product.save()
        
        # return to the products page
        return redirect(reverse('all_products'))
        
    else:
        # otherwise return an instance of the review form
        form = ReviewForm(instance=review)
        
        # return to the reviewform.html page with the form instance
        return render(request, 'reviewform.html', {'form': form})


# EDIT A REVIEW - you must be logged
@login_required
def edit_review(request, pk):
    
    # get an instance of the review
    review = get_object_or_404(Review, pk=pk) if pk else None
    # current rating of the product being reviewed
    original_review_rating = review.rating
    
    # you can only edit a review if you are the person who created the review
    if review.user == request.user:
        # if it is a POST method
        if request.method == "POST":
            
            # assign POST values, FILES and an instance of the review to form
            form = ReviewForm(request.POST, request.FILES, instance=review)
            # if the form is valid
            if form.is_valid():
                
                #save the form
                review = form.save()
                
                # if the rating has changed to the original review rating recalculate the average
                if review.rating != original_review_rating:
                   
                    # calculating the average rating of the product
                    # subtract the old rating, add the new rating and recalculate the average
                    
                    # product being reviewd
                    product = review.product
                    # new review rating 
                    review_rating = review.rating
                    # number of ratings the product has had
                    num_of_ratings = product.num_of_ratings
                    # the products average rating
                    average = product.average_rating
                    
                    # if the number of ratings equals 1 then this is the only review so the average is equal to this reviews rating
                    if num_of_ratings == 1:
                        average = review_rating
                        
                    # otherwise
                    else:
                        # subtract the old rating and recalcualte the average
                        average = ((average * num_of_ratings) - original_review_rating) / (num_of_ratings-1);
                        # add the new rating and recalculate the average
                        average = average + ((review_rating - average) / num_of_ratings)
        
                        
                    # assign the new average to the product
                    product.average_rating = average   
                    # save the product's new average in the database
                    product.save()
            
            # return to the customer profile
            return redirect(reverse('customer_profile'))
            
        else:
            # otherwise get an instance of the review form and show it in the reviewform.html page
            form = ReviewForm(instance=review)
            return render(request, 'reviewform.html', {'form': form})
    
    else:
        # information message to be shown to the user
        messages.info(request,'You are not authorised to edit this review')
        # if the logged in user is not the user who wrote the review they can not edit the review and will be returned to the index page
        return redirect(reverse('index'))
    
# view to view all reviews of a product
def view_reviews(request, id, pk=None):
    
    # get an instance of the product 
    item = get_object_or_404(Product, pk=id)
    # filter all reviews that were made about this product
    reviews = Review.objects.filter(product = item)
    # return the filtered reviews to be shown on allreviews.html
    return render(request, 'allreviews.html', {'reviews': reviews})
    

# view a review in full
def full_review(request, pk):
    
    # get an instance of the review
    review = get_object_or_404(Review, pk=pk)
    # return the review to be shown on fullreview.html
    return render(request, "fullreview.html", {'review':review})

# delete a review ( you must be logged in to delete a review)
@login_required
def delete_review(request, pk):
    
    # get an instance of the review
    review = get_object_or_404(Review, pk=pk)
    
    # you can only delete a review if you are the person who created the review or you are a staff member
    if review.user == request.user or request.user.is_staff:
       
        # the product being reviewed
        product = review.product
        # the rating this review gave the product
        review_rating = review.rating
        # number of reviews the product had before deletion
        num_of_ratings = product.num_of_ratings
        # number of reviews the product had after deletion (-1)
        new_num_of_ratings = num_of_ratings - 1
        # the average rating the product had before deletion
        average = product.average_rating
        
        # if the new number of ratings is equal to 0 then the product has no reviews so the average is equal to 0
        if new_num_of_ratings == 0:
            average = 0
        
        # otherwise recalculate the products average rating after the deletion of this review rating
        else:    
            average = ((average * num_of_ratings) - review_rating) / (new_num_of_ratings);
       
        # assign the new number of ratings for the product
        product.num_of_ratings = new_num_of_ratings
        # assign the new average rating for the product
        product.average_rating = average   
        # save the new figures to the appropriate fields in the product database
        product.save()
        # delete the review
        review.delete()
        
        # information message to be shown
        messages.success(request, 'your review was deleted')
        
        # return to the profile page
        return redirect(reverse('customer_profile'))
    
    else:
        # information message to be shown to the user
        messages.info(request,'You are not authorised to delete this review')
        # If the user trying to delete the review is not the user who created the review do not let them delete the review and return to the home page
        return redirect(reverse('index'))
    