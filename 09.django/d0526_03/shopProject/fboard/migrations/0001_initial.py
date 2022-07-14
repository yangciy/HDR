# Generated by Django 4.0.4 on 2022-05-25 02:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_alter_member_createdate_alter_member_updatedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fboard',
            fields=[
                ('f_no', models.AutoField(primary_key=True, serialize=False)),
                ('f_title', models.CharField(max_length=1000)),
                ('f_content', models.TextField()),
                ('f_group', models.IntegerField(default=0)),
                ('f_step', models.IntegerField(default=0)),
                ('f_indent', models.IntegerField(default=0)),
                ('f_hit', models.IntegerField(default=1)),
                ('f_createdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 11, 5, 57, 567839))),
                ('f_updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 11, 5, 57, 567851))),
                ('f_file', models.ImageField(blank=True, upload_to='')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
