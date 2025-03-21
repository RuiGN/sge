from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'product_id', 'quantity_size_p', 'quantity_size_m', 'quantity_size_g', 'quantity_size_gg', 'created_at', 'updated_at',)
    search_fields = ('supplier__name', 'product__title',)


admin.site.register(models.Inflow, InflowAdmin)
