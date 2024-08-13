from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.models import Category, Product


@admin.register(Category)
class CategoryModelAdmin(ImportExportModelAdmin):
    actions = ['export_as_csv']

    def get_queryset(self, request):
        return super().get_queryset(request).filter(parent__isnull=True)


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin):
