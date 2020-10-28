from django.contrib import admin

from .models import Order
from .models import OrderItem
from .models import Product

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)