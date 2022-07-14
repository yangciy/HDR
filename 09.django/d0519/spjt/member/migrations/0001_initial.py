# Generated by Django 4.0.4 on 2022-05-19 06:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_no', models.AutoField(primary_key=True, serialize=False)),
                ('m_id', models.CharField(max_length=30)),
                ('m_pw', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('m_tel', models.CharField(max_length=13)),
                ('m_zipcode', models.CharField(max_length=5)),
                ('m_address1', models.CharField(max_length=1000)),
                ('m_address2', models.CharField(max_length=1000)),
                ('m_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 15, 38, 48, 991084))),
            ],
        ),
    ]
