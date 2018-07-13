from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product 
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages

'''
REVIEW VIEWS
'''

@login_required()
def new_review(request, id, pk=None):
    """ 
    a view for creating a new post or editing a post 
    """
 
    product = get_object_or_404(Product, pk=id)
    review = get_object_or_404(Review, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = request.user
            
            review_rating = review.rating
            num_of_ratings = product.num_of_ratings
            new_num_of_ratings = num_of_ratings + 1
            average = product.average_rating
            
            average = average + ((review_rating - average) / new_num_of_ratings)
               
            product.num_of_ratings = new_num_of_ratings
            product.average_rating = average
                
            review.save()
            product.save()
        return redirect(reverse('index'))
        
    else:
        form = ReviewForm(instance=review)
        return render(request, 'reviewform.html', {'form': form})


def edit_review(request, pk):
    
    review = get_object_or_404(Review, pk=pk) if pk else None
    original_review_rating = review.rating
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            
            if review.rating != original_review_rating:
               
                # calculating the average rating of the product
                # subtract the old rating from the average and adding the new rating to the average
                product = review.product
                review_rating = review.rating
                num_of_ratings = product.num_of_ratings
                average = product.average_rating
                
                if (num_of_ratings-1)== 0:
                    average = average + ((review_rating - average) / num_of_ratings)
                    
                else:
                    average = ((average * num_of_ratings) - original_review_rating) / (num_of_ratings-1);
                    average = average + ((review_rating - average) / num_of_ratings)
    
                    
              
                product.average_rating = average   
                product.save()
            
        return redirect(reverse('index'))
        
    else:
        form = ReviewForm(instance=review)
        return render(request, 'reviewform.html', {'form': form})


def view_reviews(request, id, pk=None):
    
    item = get_object_or_404(Product, pk=id)
    reviews = Review.objects.filter(product = item)
    return render(request, 'allreviews.html', {'reviews': reviews})
    

def full_review(request, pk):
    
    review = get_object_or_404(Review, pk=pk)
    return render(request, "fullreview.html", {'review':review})

def delete_review(request, pk):
    
    review = get_object_or_404(Review, pk=pk)
    
    # calculating the average rate of the product again as a rating is deleted 
    product = review.product
    review_rating = review.rating
    num_of_ratings = product.num_of_ratings
    new_num_of_ratings = num_of_ratings - 1
    average = product.average_rating
    if new_num_of_ratings == 0:
        average = 0
    else:    
        average = ((average * num_of_ratings) - review_rating) / (new_num_of_ratings);
   
    product.num_of_ratings = new_num_of_ratings
    product.average_rating = average   
    
    product.save()
    review.delete()
    
    messages.success(request, 'your review was deleted')
    
    return redirect(reverse('index'))
    
    
    
    
    
    
    
    

    
    
    
    