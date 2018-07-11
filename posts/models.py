from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# a blog post model

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True)
    view_on_front_page = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title