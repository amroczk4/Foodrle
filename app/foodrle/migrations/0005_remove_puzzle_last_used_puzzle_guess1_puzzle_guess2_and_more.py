# Generated by Django 4.1.1 on 2022-11-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrle', '0004_alter_dishes_calories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzle',
            name='last_used',
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess1',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess2',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess3',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess4',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess5',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='guess6',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
