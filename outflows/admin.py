from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_id', 'quantity_size_p', 'quantity_size_m', 'quantity_size_g', 'quantity_size_gg', 'description', 'payment_type', 'customer_name', 'customer_phone', 'created_at',)
    search_fields = ('product__title',)


admin.site.register(models.Outflow, OutflowAdmin)
