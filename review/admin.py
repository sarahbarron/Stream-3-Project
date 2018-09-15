from django.contrib import admin
from .models import Review

''' registering the Review model so that it will be 
shown in the admin panel '''

admin.site.register(Review)
