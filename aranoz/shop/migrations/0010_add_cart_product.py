# Generated by Django 5.0.6 on 2024-07-02 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_add_cart_qty_add_cart_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
