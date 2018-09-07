from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# a blog post model

# Model for Posts
class Post(models.Model):
    
    # title of the post
    title = models.CharField(max_length=200)
    
    # the posts content
    content = RichTextUploadingField(blank=True, null=True)
    
    # the date the post was created
    created_date = models.DateTimeField(auto_now_add=True)
    
    # the date the post was published
    published_date = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    
    # the number of views the post has had
    views = models.IntegerField(default=0)
    
    # post tags
    tag = models.CharField(max_length=30, blank=True, null=True)
    
    # category the post is in
    category = models.CharField(max_length=30, blank=True, null=True)
    
    # the post image
    image = models.ImageField(upload_to="img", blank=True)
    
    # if the post is to be viewed on the front page or not
    view_on_front_page = models.BooleanField(default=True)

    # return the title
    def __str__(self):
        return self.title