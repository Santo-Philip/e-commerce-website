# Generated by Django 4.1.1 on 2022-09-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
