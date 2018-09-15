from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

'''
VIEWS FOR BLOG POSTS
'''


def get_posts(request):
    ''' return a list of all posts and show on blogposts.html.
    filter the posts that were created previous to the current
    time and order them by the date they were published in
    decending order '''

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "allposts.html", {'posts': posts})


def post_full(request, pk):
    ''' returns full view of a post '''

    # an instance of the post
    post = get_object_or_404(Post, pk=pk)
    # increment the number of views of the post by 1
    post.views += 1
    # save the post
    post.save()
    # return the post and show it on fullpost.html
    return render(request, "fullpost.html", {'post': post})


# create a new post or edit a post
@login_required
def create_or_edit_post(request, pk=None):
    ''' create or edit a post
    login required and staff member status required '''

    # only a staff memeber can create or edit a post
    if request.user.is_staff:
        # return an instance of Post
        post = get_object_or_404(Post, pk=pk) if pk else None
        # if it is a POST method
        if request.method == "POST":
            # get an instance of the BlogPostForm
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            # if the form is valid
            if form.is_valid():
                # save the form
                post = form.save()
                # redirect to post_full with the post primary key
                return redirect(post_full, post.pk)
        else:
            # otherwise return an instance of the BlogPostForm
            form = BlogPostForm(instance=post)
        # return to the blogpostform.html page with the form
        return render(request, 'blogpostform.html', {'form': form})
    else:
        messages.info(request, 'You are not authorised to create or '
                      'edit posts')
        # if they are not a staff memeber return to the homepage
        return redirect(reverse('index'))


@login_required
def delete_post(request, pk):
    ''' view to delete a post login and staff member access is required '''

    # only a staff memeber can delete a post
    if request.user.is_staff:
        # get the post object with the primary key
        post = get_object_or_404(Post, pk=pk)
        # delete the post
        post.delete()
        # alert with the following message that the post has been deleted
        messages.success(request, 'your post was deleted')
        # return to the home page
        return redirect(reverse('get_posts'))
    else:
        messages.info(request, 'You are not authorised to delete posts')
        # if they are not a staff memeber return to the homepage
        return redirect(reverse('index'))
