# Generated by Django 4.1.1 on 2022-10-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrle', '0005_rename_user_id_userstats_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]