# Generated by Django 4.2.4 on 2023-10-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_tag_remove_blog_category_remove_blog_dislike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
