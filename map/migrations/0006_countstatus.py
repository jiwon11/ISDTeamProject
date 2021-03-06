# Generated by Django 3.2.3 on 2021-06-12 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_alter_mapcity_geometry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountStatus',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('add', models.IntegerField(default=0)),
                ('accumulation', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.mapcity')),
            ],
        ),
    ]
