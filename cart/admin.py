from django.contrib import admin

from cart.models import Order, CartItem

admin.site.register(Order)
admin.site.register(CartItem)
