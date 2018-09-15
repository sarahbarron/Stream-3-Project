from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInLine(admin.TabularInline):
    ''' template used to render the Order in the admin interface '''

    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )
    ''' Inlines to edit customer details & payment details at the same time.'''


# registering the Order and OrderAdmin models
# so that it will be shown in the admin panel
admin.site.register(Order, OrderAdmin)
