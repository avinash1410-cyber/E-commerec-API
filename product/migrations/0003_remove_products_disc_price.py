# Generated by Django 4.0.4 on 2022-04-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products_disc_price_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='disc_price',
        ),
    ]