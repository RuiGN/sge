# Generated by Django 5.0.1 on 2025-01-08 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
