from django.conf.urls import url
from .views import new_review, edit_review, view_reviews, full_review, delete_review

urlpatterns=[
    url(r'^reviews/(?P<id>\d+)$', view_reviews, name='view_reviews'),
    url(r'^(?P<pk>\d+)/$', full_review, name = 'full_review'),
    url(r'^new/(?P<id>\d+)$', new_review, name='new_review'),
    url(r'^(?P<pk>\d+)/edit/$', edit_review, name='edit_review'),
    url(r'^(?P<pk>\d+)/delete/$', delete_review, name='delete_review'),
    ]
