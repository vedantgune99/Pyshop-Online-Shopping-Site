# Generated by Django 4.0.5 on 2022-06-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_rename_item_id_cart_price_cart_image_cart_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]