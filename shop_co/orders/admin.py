from django.contrib import admin
from .models import Order, Order_item, Shipping

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Shipping)