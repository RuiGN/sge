# Generated by Django 5.0.1 on 2025-01-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outflow',
            name='quantity',
        ),
        migrations.AddField(
            model_name='outflow',
            name='quantity_size_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outflow',
            name='quantity_size_gg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outflow',
            name='quantity_size_m',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outflow',
            name='quantity_size_p',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
