from django.db import models
from products.models import Product

CHOICES = (('À VISTA', 'À VISTA'), ('A PRAZO', 'A PRAZO'), ('A RECEBER À VISTA', 'A RECEBER À VISTA'))


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    quantity_size_p = models.IntegerField()
    quantity_size_m = models.IntegerField()
    quantity_size_g = models.IntegerField()
    quantity_size_gg = models.IntegerField()
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    outflow_cost_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Preço de Custo')
    outflow_selling_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Preço de Venda')
    payment_type = models.CharField(max_length=100, null=False, blank=False, choices=CHOICES, verbose_name='Pagamento')
    customer_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome do Cliente')
    customer_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telefone do Cliente')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Saídas'

    def __str__(self):
        return str(self.product)
