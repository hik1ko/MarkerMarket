from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, Category, Tag, AdPost, Cart
from apps.models import Product, Category, Tag, Address


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class Tag(ModelAdmin):
    pass


@admin.register(AdPost)
class AdPost(ModelAdmin):
    pass


@admin.register(Cart)
class Cart(ModelAdmin):
    pass


@admin.register(Address)
class Address(ModelAdmin):
    pass
