# Generated by Django 4.2.4 on 2023-11-03 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_subscribe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='Subscriber',
        ),
    ]
