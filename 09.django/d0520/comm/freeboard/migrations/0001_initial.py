# Generated by Django 4.0.4 on 2022-05-20 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('f_no', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=100)),
                ('f_title', models.CharField(max_length=1000)),
                ('f_content', models.TextField()),
                ('f_group', models.IntegerField()),
                ('f_step', models.IntegerField()),
                ('f_indent', models.IntegerField()),
                ('f_hit', models.IntegerField(default=1)),
                ('f_createdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 20, 10, 52, 55, 207812))),
                ('f_updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 20, 10, 52, 55, 207831))),
                ('f_file', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
