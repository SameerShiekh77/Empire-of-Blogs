# Generated by Django 4.2.4 on 2024-08-19 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 19, 10, 1, 33, 202072)),
        ),
    ]
