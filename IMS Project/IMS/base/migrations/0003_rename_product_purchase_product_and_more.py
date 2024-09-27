# Generated by Django 5.1.1 on 2024-09-27 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='Vendor',
            new_name='vendor',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='Quantity',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(to='base.department'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.producttype'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.FloatField(null=True),
        ),
    ]
