# Generated by Django 4.1.1 on 2022-09-26 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0003_alter_category_options_alter_category_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]
