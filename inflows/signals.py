from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity_size_p > 0:
            product = instance.product
            product.quantity_size_p += instance.quantity_size_p
            product.save()
        if instance.quantity_size_m > 0:
            product = instance.product
            product.quantity_size_m += instance.quantity_size_m
            product.save()
        if instance.quantity_size_g > 0:
            product = instance.product
            product.quantity_size_g += instance.quantity_size_g
            product.save()
        if instance.quantity_size_gg > 0:
            product = instance.product
            product.quantity_size_gg += instance.quantity_size_gg
            product.save()
