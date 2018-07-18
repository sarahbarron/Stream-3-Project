from django.conf.urls import url
from .views import get_posts, post_full, create_or_edit_post,delete_post

urlpatterns=[
    
    # url to return all posts
    url(r'^$', get_posts, name='get_posts'),
    
    # url to view a particular post
    url(r'^(?P<pk>\d+)/$', post_full, name = 'post_detail'),
    
    # url to create a post
    url(r'^new/$', create_or_edit_post, name='new_post'),
    
    # url to edit a post
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    
    # url to delete a post
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post')
    ]
