# Generated by Django 4.1.1 on 2022-11-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodrle', '0005_remove_puzzle_last_used_puzzle_guess1_puzzle_guess2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='dish',
            new_name='ans_dish',
        ),
    ]
