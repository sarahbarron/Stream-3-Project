from django.shortcuts import render
from posts.models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
# index page view 
def index(request):
  
    posts = Post.objects.filter(view_on_front_page = True).order_by('-published_date')[:3]
    posts2 = Post.objects.filter(view_on_front_page = True).order_by('-published_date')[3:6]
     # paginator for myorders with 5 orders per page
    
    return render(request, "index.html", {'posts': posts, 'posts2': posts2})
    
   
    
#treatments page view
def treatments(request):
    #views to retrieve the index.html page
    return render(request, "treatments.html")