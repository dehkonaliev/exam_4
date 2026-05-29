from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at']
    search_fields = ['name', 'desc']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
