# Generated by Django 4.2.4 on 2024-06-23 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_bannners_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannners',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 10, 41, 29, 328017, tzinfo=datetime.timezone.utc)),
        ),
    ]
