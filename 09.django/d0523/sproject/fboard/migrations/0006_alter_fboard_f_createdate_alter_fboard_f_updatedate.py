# Generated by Django 4.0.4 on 2022-05-24 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0005_alter_fboard_f_createdate_alter_fboard_f_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 24, 11, 43, 3, 299284)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 24, 11, 43, 3, 299294)),
        ),
    ]
