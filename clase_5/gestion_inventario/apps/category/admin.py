from django.contrib import admin

from apps.category.models import Category, CategoryItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)


@admin.register(CategoryItem)
class CategoryItem(admin.ModelAdmin):
    list_display = ('category', 'item')
    search_fields = ('category__name', 'item__name')
    list_filter = ('category__name', 'item__name')