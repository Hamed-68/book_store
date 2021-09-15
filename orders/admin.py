from django.contrib import admin
from .models import OrderItem, Order, PointDiscount

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(PointDiscount)
