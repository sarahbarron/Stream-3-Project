from django.shortcuts import render, redirect, reverse
from posts.models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    ''' view to direct to the index.html page '''

    # posts to be shown on the landing page news &
    # special offers section 1st 3 most recent
    # front page posts
    posts = Post.objects.filter(view_on_front_page=True).order_by('-published_date')[:3]
    # next 3 most recent front page posts
    posts2 = Post.objects.filter(view_on_front_page=True).order_by('-published_date')[3:6]
    # go to the index.html page with the 6 most
    # recent posts to be shown on the landing page.
    return render(request, "index.html", {'posts': posts, 'posts2': posts2})


def treatments(request):
    ''' view to the treatments.html page '''

    return render(request, "treatments.html")
