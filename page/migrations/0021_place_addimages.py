# Generated by Django 4.0.2 on 2022-09-25 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0020_alter_imagecollection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='addImages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collection', to='page.imagecollection'),
        ),
    ]
