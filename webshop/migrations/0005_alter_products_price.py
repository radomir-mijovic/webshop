# Generated by Django 4.0.1 on 2022-02-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0004_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(),
        ),
    ]
