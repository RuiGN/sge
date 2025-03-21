from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'category', 'serie_number',)
    search_fields = ('title', 'id')


admin.site.register(models.Product, ProductAdmin)
