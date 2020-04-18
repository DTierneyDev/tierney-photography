from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    """ Get the OrderLineItem to be shown in the Order model in admin """
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    """ add OrderLineItems above to the orders """
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
