# Generated by Django 4.0.4 on 2022-04-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='disc',
            field=models.FloatField(default=1, null=True),
        ),
    ]
