from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import AdPost, Cart, Product, Category, Address, ProductImage


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = 'slug',


class ProductImageModelAdmin(StackedInline):
    model = ProductImage,


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    exclude = 'slug',
    inlines = ProductImageModelAdmin,


@admin.register(AdPost)
class AdPost(ModelAdmin):
    pass


@admin.register(Cart)
class Cart(ModelAdmin):
    pass


@admin.register(Address)
class Address(ModelAdmin):
    pass
