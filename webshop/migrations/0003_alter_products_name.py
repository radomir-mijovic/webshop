# Generated by Django 4.0.1 on 2022-01-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_alter_products_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
