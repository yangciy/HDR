# Generated by Django 4.0.4 on 2022-05-30 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0003_alter_fboard_f_createdate_alter_fboard_f_updatedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='c_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 50, 55, 880912)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 50, 55, 880570)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 50, 55, 880580)),
        ),
    ]
