# Generated by Django 3.2.3 on 2021-06-06 17:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapCity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sigungu_en', models.CharField(db_column='sigungu_EN', max_length=200)),
                ('sigungu_kr', models.DateTimeField(db_column='sigungu_KR')),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
