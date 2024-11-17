# Generated by Django 5.0.1 on 2024-11-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("outflows", "0002_outflow_outflow_cost_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="outflow",
            name="payment_type",
            field=models.TextField(default="À VISTA", verbose_name="Pagamento"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="outflow",
            name="outflow_cost_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=20,
                verbose_name="Preço de Custo",
            ),
        ),
        migrations.AlterField(
            model_name="outflow",
            name="outflow_selling_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=20,
                verbose_name="Preço de Venda",
            ),
        ),
    ]
