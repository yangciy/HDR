# Generated by Django 4.0.4 on 2022-05-25 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 14, 45, 34, 204679)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 14, 45, 34, 204689)),
        ),
    ]
