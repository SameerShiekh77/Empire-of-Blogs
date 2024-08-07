# Generated by Django 4.2.4 on 2024-08-04 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_alter_bannners_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageAdPlacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=200)),
                ('ad_link', models.URLField()),
                ('ad_image', models.FileField(upload_to='home-advert')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Home Page Ad Placement',
            },
        ),
        migrations.AlterField(
            model_name='bannners',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 4, 19, 2, 57, 416946, tzinfo=datetime.timezone.utc)),
        ),
    ]
