# Generated by Django 4.0.5 on 2022-06-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_remove_cart_quantity_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
