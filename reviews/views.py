from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product 
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required

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
            review.save()
        return redirect(reverse('index'))
        
    else:
        form = ReviewForm(instance=review)
        return render(request, 'reviewform.html', {'form': form})


def edit_review(request, pk):
    
    review = get_object_or_404(Review, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        
        if form.is_valid():
            review = form.save()
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
    
    
    
    
    