# Generated by Django 4.0.4 on 2022-05-23 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_alter_member_mcreatedate_alter_member_mupdatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mCreatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 11, 3, 45, 222343)),
        ),
        migrations.AlterField(
            model_name='member',
            name='mUpdatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 11, 3, 45, 222343)),
        ),
    ]
