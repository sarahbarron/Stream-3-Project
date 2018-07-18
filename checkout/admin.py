from django.contrib import admin
from .models import Order, OrderLineItem

# template used to render the Order in the admin interface
class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem
    
'''
Inlines to edit customer details & payment details at the same time.
'''
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )

# registering the Order and OrderAdmin models so that it will be shown in the admin panel
admin.site.register(Order, OrderAdmin)
