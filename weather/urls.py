from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path("", views.home, name="home"),
    path("add-weather", views.add_weather, name="add-weather-data"),
    path("display", views.display_weather, name="display-weather"),
]
