from django.contrib import admin
from .models import CartItem, CustomerProfile

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'quantity', 'price', 'created_at']
    search_fields = ['user__username', 'product_name']

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'created_at']
    search_fields = ['user__username', 'phone', 'city']
