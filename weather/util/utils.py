import random

import requests
from django.conf import settings
from django.forms.models import model_to_dict


def get_city_weather_dict(model):
    """converts model instance data to dict then adds model's city data"""
    city_data = {"name": model.city.name, "coord": model.city.coord}
    data_dict = model_to_dict(model)
    return {**data_dict, **city_data}


def random_user_agents():
    """returns random user-agents from the list"""
    UA = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    ]

    return random.choice(UA)


def get_city_weather(city_name: str):
    try:
        headers = {"User-Agent": random_user_agents()}
        OPENWEATHER_API_KEY = settings.OPENWEATHER_API_KEY
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric",
            headers=headers,
        )

        if response.status_code == 200:
            data_json = response.json()

            city_data = {
                "name": data_json["name"],
                "country_code": data_json["sys"]["country"],
                "coord": str(data_json["coord"]["lon"])
                + ", "
                + str(data_json["coord"]["lat"]),
            }

            weather_json = {
                "temp_max": data_json["main"]["temp_max"],
                "temp_min": data_json["main"]["temp_min"],
                "temp_feels": data_json["main"]["feels_like"],
                "pressure": data_json["main"]["pressure"],
                "humidity": data_json["main"]["humidity"],
                "weather_main": data_json["weather"][0]["main"],
                "desc": data_json["weather"][0]["description"],
                "icon": data_json["weather"][0]["icon"],
                "wind": data_json["wind"]["speed"],
            }
            return city_data, weather_json
    except requests.ConnectionError:
        return None
