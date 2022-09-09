# Generated by Django 4.0.2 on 2022-09-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_place_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='City_name',
        ),
        migrations.RenameField(
            model_name='governorate',
            old_name='name',
            new_name='Governorate_Name',
        ),
        migrations.AddField(
            model_name='phone',
            name='phone3',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='instagram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]