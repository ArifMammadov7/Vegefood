# Generated by Django 4.2.4 on 2023-10-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_setting_description_az_setting_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
