from django.contrib import admin
from .models import menu_data,wishlist,cart_data,order_data
# Register your models here.
admin.site.register(menu_data)
admin.site.register(wishlist)
admin.site.register(cart_data)
admin.site.register(order_data)