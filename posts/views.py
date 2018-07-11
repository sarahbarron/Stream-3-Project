from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.models import User

'''
VIEWS FOR BLOG POSTS
'''

def get_posts(request):
    
    """ 
    return a list of all posts and show on blogposts.html. filter the posts that were created previous to the current time and order them by the date they were published in decending order
    """
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "allposts.html", {'posts': posts})


def post_full(request, pk):
   """
    a single post object with a post id, show on postdetail.html or return an error if the post is not found. increment the number of views by 1
   """
   
   post = get_object_or_404(Post, pk=pk)
   post.views += 1
   post.save()
   return render(request, "fullpost.html", {'post':post})


def create_or_edit_post(request, pk=None):
    """ 
    a view for creating a new post or editing a post 
    """
    if request.user.is_staff:
    
        post = get_object_or_404(Post, pk=pk) if pk else None
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(post_full, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form})
    
    else:
        return redirect(reverse('index'))
        
        
        
    