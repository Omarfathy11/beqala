# Generated by Django 4.0.2 on 2022-09-08 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_rename_name_city_city_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='name',
            new_name='Place_Name',
        ),
    ]
