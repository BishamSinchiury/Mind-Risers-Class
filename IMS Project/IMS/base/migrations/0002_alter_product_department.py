# Generated by Django 5.1.1 on 2024-09-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(null=True, to='base.department'),
        ),
    ]
