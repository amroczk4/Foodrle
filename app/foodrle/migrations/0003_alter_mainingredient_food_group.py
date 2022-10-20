# Generated by Django 4.1.1 on 2022-10-18 08:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrle', '0002_rename_dish_id_puzzle_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainingredient',
            name='food_group',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
    ]