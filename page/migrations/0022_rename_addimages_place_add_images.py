# Generated by Django 4.0.2 on 2022-09-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0021_place_addimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='addImages',
            new_name='add_images',
        ),
    ]