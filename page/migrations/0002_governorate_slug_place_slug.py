# Generated by Django 4.0.2 on 2022-09-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='governorate',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
