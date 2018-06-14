from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category','tag', 'published_date', 'view_on_front_page')
        
