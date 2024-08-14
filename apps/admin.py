from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass
