# Generated by Django 4.0.2 on 2022-09-08 23:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_address_city_alter_address_line1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, upload_to=''), size=8), size=8),
        ),
    ]
