# Generated by Django 3.2.8 on 2021-10-10 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]