# Generated by Django 4.0.2 on 2022-09-08 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_resturant_atmosphere_alter_resturant_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.city'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='city',
            name='governorate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.governorate'),
        ),
    ]
