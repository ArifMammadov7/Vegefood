# Generated by Django 4.2.4 on 2023-10-31 17:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_about_delete_discounts_delete_homecategoriesimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content_az',
            field=ckeditor.fields.RichTextField(help_text='CONTENT COLUMN ', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_en',
            field=ckeditor.fields.RichTextField(help_text='CONTENT COLUMN ', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ru',
            field=ckeditor.fields.RichTextField(help_text='CONTENT COLUMN ', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
