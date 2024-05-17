from django.contrib import admin
from menu.models import Product, Category, Table

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Table)
