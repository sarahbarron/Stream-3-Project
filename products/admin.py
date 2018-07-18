from django.contrib import admin
from .models import Product

# registering the Product model so that it will be shown in the admin panel
admin.site.register(Product)
