# Generated by Django 4.2.4 on 2024-08-19 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_coupon_usage_count_alter_bannners_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannners',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 19, 5, 23, 54, 323955, tzinfo=datetime.timezone.utc)),
        ),
    ]
