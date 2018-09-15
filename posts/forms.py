from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    ''' form for creating a blog post '''

    class Meta:
        # form is based on the Post model
        model = Post
        # fields to be included
        fields = ('title',
                  'content',
                  'image',
                  'category',
                  'tag',
                  'published_date',
                  'view_on_front_page')
