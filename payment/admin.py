from django.contrib import admin

from payment.models import Item, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_create', 'date_change', 'customer']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['name', 'price']
    list_editable = ['price', 'description']


admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
