from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


