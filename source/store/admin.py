from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'created')
    search_fields = ('title', 'description')
    list_filter = ('category', 'created')
    ordering = ('-created',)

admin.site.register(Product, ProductAdmin)
