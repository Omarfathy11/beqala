# Generated by Django 4.0.2 on 2022-09-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0019_alter_imagecollection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecollection',
            name='image',
            field=models.ImageField(null=True, upload_to='places/'),
        ),
    ]
