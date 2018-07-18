from django.conf.urls import url
from .views import new_review, edit_review, view_reviews, full_review, delete_review

urlpatterns=[
    # url to view all reviews for a certain product
    url(r'^(?P<id>\d+)/$', view_reviews, name='view_reviews'),
    
    # url to view a full review 
    url(r'^full_review/(?P<pk>\d+)/$', full_review, name = 'full_review'),
    
    # url to create a new review
    url(r'^new/(?P<id>\d+)/$', new_review, name='new_review'),
    
    # url to edit a review
    url(r'^edit/(?P<pk>\d+)/$', edit_review, name='edit_review'),
    
    # url to delete a review
    url(r'^delete/(?P<pk>\d+)/$', delete_review, name='delete_review'),
    ]
