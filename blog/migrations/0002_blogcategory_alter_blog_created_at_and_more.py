# Generated by Django 4.2.4 on 2024-06-23 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 13, 41, 22, 157894)),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ManyToManyField(blank=True, to='blog.blogcategory'),
        ),
    ]
