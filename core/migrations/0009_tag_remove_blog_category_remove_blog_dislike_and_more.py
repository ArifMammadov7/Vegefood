# Generated by Django 4.2.4 on 2023-10-29 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='view',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='core.tag'),
            preserve_default=False,
        ),
    ]