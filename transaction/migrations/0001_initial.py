# Generated by Django 4.2 on 2024-08-03 17:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_alter_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='inventory')),
                ('entrance', models.BooleanField(default=True, verbose_name='entrance')),
                ('transaction_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Transaction Time')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'transactiones',
            },
        ),
    ]