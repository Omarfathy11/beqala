# Generated by Django 4.0.2 on 2022-09-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_alter_imagecollection_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecollection',
            name='image',
            field=models.ImageField(null=True, upload_to='places/'),
        ),
    ]
