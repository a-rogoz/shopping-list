from django.contrib import admin

from .models import (
    ShoppingList,
    Product
)


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]
    date_hierarchy = 'created_at'
    list_display = ('id', 'name', 'user', 'created_at')
    list_display_links = ('name',)
    list_filter = ('user',)
    list_per_page = 20
    search_fields = ['name', 'user']