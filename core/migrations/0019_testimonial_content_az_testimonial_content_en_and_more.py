# Generated by Django 4.2.4 on 2023-10-31 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_blog_content_az_blog_content_en_blog_content_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='position_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='position_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='position_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]