from django.contrib import admin
from .models import Post

''' registering the Posts model
so that it will be shown in the admin panel'''

admin.site.register(Post)
