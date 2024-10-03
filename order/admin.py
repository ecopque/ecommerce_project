from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline): ##
    model = OrderItem ##
    extra = 3 ##

class OrderAdmin(admin.ModelAdmin): ##
    inlines = [OrderItemInline] ##


admin.site.register(Order, OrderAdmin) ##
admin.site.register(OrderItem) ##