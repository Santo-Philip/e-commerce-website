# Generated by Django 4.1.1 on 2022-09-26 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0005_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]