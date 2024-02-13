# Generated by Django 3.2.12 on 2024-02-06 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IngredientName', models.CharField(default='Generic Ingredient', max_length=255)),
                ('Quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='CategoryName',
            field=models.CharField(default='Generic Category', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.category'),
        ),
        migrations.AddField(
            model_name='item',
            name='Description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AddField(
            model_name='item',
            name='ItemName',
            field=models.CharField(default='Generic Item', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='PreparationTime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MenuName', models.CharField(default='Generic Menu', max_length=255)),
                ('Description', models.TextField(default='No description available.')),
                ('Price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Available', models.BooleanField(default=True)),
                ('CreationDate', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient')),
                ('Item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.item')),
            ],
        ),
    ]
