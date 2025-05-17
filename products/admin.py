from django.contrib import admin

from products.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ex_date', 'country', 'price', 'category')
    list_filter = ('name', 'country', 'price', 'category')
    search_fields = ('id', 'name', 'ex_date', 'country', 'price', 'category')

admin.site.register(Products, ProductsAdmin)