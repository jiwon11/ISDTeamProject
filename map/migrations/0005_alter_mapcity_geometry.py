# Generated by Django 3.2.3 on 2021-06-07 00:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_alter_mapcity_geometry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapcity',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
    ]
