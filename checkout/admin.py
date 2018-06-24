from django.contrib import admin
from .models import Order, OrderLineItem

# template used to render the Order in the admin interface
class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem
    
'''
the admin interface has the ability to edit more than 1 model on a single page. 
This is known as inlines we need this for customer details & payment details.
'''
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )

admin.site.register(Order, OrderAdmin)
