# Generated by Django 4.2.4 on 2024-12-28 09:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_accessurls_alter_bannners_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannners',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 28, 9, 38, 17, 436168, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='cms.store')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
