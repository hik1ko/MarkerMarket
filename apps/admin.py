from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, Category, Tag, ad_post, Cart


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class Tag(ModelAdmin):
    pass


@admin.register(ad_post)
class ad_post(ModelAdmin):
    pass


@admin.register(Cart)
class Cart(ModelAdmin):
    pass
