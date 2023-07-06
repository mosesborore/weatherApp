# Generated by Django 3.2.4 on 2023-06-21 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "city_id",
                    models.BigAutoField(
                        auto_created=True,
                        db_column="City_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_column="City_name", max_length=64, verbose_name="City Name"
                    ),
                ),
                ("coord", models.CharField(db_column="City_coord", max_length=64)),
                (
                    "country_code",
                    models.CharField(db_column="City_country_code", max_length=6),
                ),
            ],
            options={
                "verbose_name_plural": "Cities",
                "db_table": "City",
            },
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "weather_id",
                    models.BigAutoField(
                        auto_created=True,
                        db_column="Weather_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temp_min", models.BigIntegerField(db_column="Weather_temp_min")),
                ("temp_max", models.BigIntegerField(db_column="Weather_temp_max")),
                (
                    "temp_feels",
                    models.DecimalField(
                        db_column="Weather_temp_feels", decimal_places=2, max_digits=5
                    ),
                ),
                ("pressure", models.PositiveIntegerField(db_column="Weather_pressure")),
                ("humidity", models.PositiveIntegerField(db_column="Weather_humidity")),
                (
                    "weather_main",
                    models.CharField(db_column="Weather_weather_main", max_length=64),
                ),
                ("desc", models.CharField(db_column="Weather_desc", max_length=64)),
                ("icon", models.CharField(db_column="Weathera_icon", max_length=10)),
                (
                    "wind",
                    models.DecimalField(
                        db_column="Weather_wind", decimal_places=2, max_digits=5
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True, db_column="Weather_updated_at"
                    ),
                ),
                (
                    "City",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city",
                        to="weather.city",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Weather",
                "db_table": "Weather",
            },
        ),
    ]
