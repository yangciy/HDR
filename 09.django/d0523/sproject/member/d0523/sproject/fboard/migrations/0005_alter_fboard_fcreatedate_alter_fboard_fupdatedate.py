# Generated by Django 4.0.4 on 2022-05-23 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0004_alter_fboard_fcreatedate_alter_fboard_fupdatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='fCreatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 11, 4, 33, 98742)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='fUpdatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 11, 4, 33, 98742)),
        ),
    ]
