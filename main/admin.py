from django.contrib import admin

# Register your models here.

from django.contrib import admin
from main.models import Category, Product, Version


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price')
    list_filter = ('category', 'name')
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version_name', 'version_index')




