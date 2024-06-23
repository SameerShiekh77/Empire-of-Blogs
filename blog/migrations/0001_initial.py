# Generated by Django 4.2.4 on 2024-06-23 08:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, unique=True)),
                ('description', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 6, 23, 13, 10, 21, 395848))),
                ('no_of_likes', models.IntegerField(default=0)),
                ('is_latest_blog', models.BooleanField(default=False)),
                ('buy_now_button_link', models.CharField(blank=True, max_length=225, null=True)),
                ('is_buy_now_button_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
