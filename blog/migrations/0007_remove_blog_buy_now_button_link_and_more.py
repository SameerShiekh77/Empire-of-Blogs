# Generated by Django 4.2.4 on 2024-07-01 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='buy_now_button_link',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='is_buy_now_button_enabled',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 16, 4, 8, 806386)),
        ),
    ]
