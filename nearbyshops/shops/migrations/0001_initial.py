# Generated by Django 4.1 on 2022-08-31 22:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
            ],
        ),
    ]
