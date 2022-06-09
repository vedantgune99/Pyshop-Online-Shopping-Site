from django.contrib import admin
from .models import Product, ItemType, Cart

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'price', 'item_type')


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('item_type',)


admin.site.register(Cart)

admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Product, ProductAdmin)
