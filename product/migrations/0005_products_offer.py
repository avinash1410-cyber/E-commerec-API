# Generated by Django 4.0.4 on 2022-04-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_products_artist_products_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='offer',
            field=models.CharField(choices=[('first', '10'), ('second', '15'), ('third', '20'), ('fourth', '22'), ('fifth', '25')], default='Add to cart', max_length=20, null=True),
        ),
    ]