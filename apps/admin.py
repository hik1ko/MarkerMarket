from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, Category, Tag


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class Tag(ModelAdmin)
    pass


