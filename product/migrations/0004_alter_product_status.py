# Generated by Django 4.2 on 2024-08-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_phone_color_product_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Stauts'),
        ),
    ]