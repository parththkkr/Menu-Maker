# Generated by Django 3.2.12 on 2024-02-06 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20240206_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='CategoryID',
        ),
        migrations.RenameField(
            model_name='itemingredient',
            old_name='Ingredient',
            new_name='IngredientID',
        ),
        migrations.RenameField(
            model_name='itemingredient',
            old_name='Item',
            new_name='ItemID',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Category',
            new_name='CategoryID',
        ),
    ]