# Generated by Django 4.0.4 on 2022-05-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_no', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_servings', models.CharField(max_length=100)),
                ('p_unitPrice', models.IntegerField(default=0)),
                ('p_description', models.TextField()),
                ('p_category', models.CharField(max_length=20)),
                ('p_manufacturer', models.CharField(max_length=20)),
                ('p_unit', models.IntegerField(default=100)),
                ('p_filename', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
