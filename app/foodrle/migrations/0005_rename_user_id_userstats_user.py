# Generated by Django 4.1.1 on 2022-10-20 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodrle', '0004_remove_dishes_color_delete_colors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstats',
            old_name='user_id',
            new_name='user',
        ),
    ]