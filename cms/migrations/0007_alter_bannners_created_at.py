# Generated by Django 4.2.4 on 2024-07-01 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_alter_bannners_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannners',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 11, 4, 8, 805106, tzinfo=datetime.timezone.utc)),
        ),
    ]