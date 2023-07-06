from django.db import models


class City(models.Model):
    city_id = models.BigAutoField(
        db_column="City_id",
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
    )
    name = models.CharField("City Name", max_length=64, db_column="City_name")
    coord = models.CharField(max_length=64, db_column="City_coord")
    country_code = models.CharField(max_length=6, db_column="City_country_code")

    class Meta:
        verbose_name_plural = "Cities"
        db_table = "City"

    def __str__(self):
        return str(self.name)


class Weather(models.Model):
    weather_id = models.BigAutoField(
        db_column="Weather_id",
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ID",
    )
    temp_min = models.BigIntegerField(db_column="Weather_temp_min")
    temp_max = models.BigIntegerField(db_column="Weather_temp_max")
    temp_feels = models.DecimalField(
        max_digits=5, decimal_places=2, db_column="Weather_temp_feels"
    )
    pressure = models.PositiveIntegerField(db_column="Weather_pressure")
    humidity = models.PositiveIntegerField(db_column="Weather_humidity")
    weather_main = models.CharField(max_length=64, db_column="Weather_weather_main")
    desc = models.CharField(max_length=64, db_column="Weather_desc")
    icon = models.CharField(max_length=10, db_column="Weathera_icon")
    city = models.OneToOneField("City", related_name="city", on_delete=models.CASCADE)
    wind = models.DecimalField(max_digits=5, decimal_places=2, db_column="Weather_wind")
    updated_at = models.DateTimeField(db_column="Weather_updated_at", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Weather"
        db_table = "Weather"

    def __str__(self):
        return str(self.weather_id) + " - " + str(self.city.name)
