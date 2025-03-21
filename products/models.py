from django.db import models
from categories.models import Category
from brands.models import Brand


class Product(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products',)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products',)
    description = models.TextField(null=True, blank=True,)
    serie_number = models.CharField(max_length=200, null=True, blank=True,)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2,)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2,)
    cash_selling_price = models.DecimalField(max_digits=20, decimal_places=2,)
    quantity_size_p = models.IntegerField(default=0,)
    quantity_size_m = models.IntegerField(default=0,)
    quantity_size_g = models.IntegerField(default=0,)
    quantity_size_gg = models.IntegerField(default=0,)
    quantity = models.IntegerField(default=0,)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    photo = models.ImageField(upload_to='sge/', blank=True, null=True,)

    class Meta:
        ordering = ['title']
        verbose_name = 'Produtos'
        

    def __str__(self):
        return self.title
