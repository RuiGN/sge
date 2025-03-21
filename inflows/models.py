from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantity_size_p = models.IntegerField()
    quantity_size_m = models.IntegerField()
    quantity_size_g = models.IntegerField()
    quantity_size_gg = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entradas'

    def __str__(self):
        return str(self.product)
