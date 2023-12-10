from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from render_block import render_block_to_string
from .models import City, Weather
from .util import utils


def get_city_weather_from_db(city_name: str):
    """fetch data from db"""
    try:
        weather = Weather.objects.get(city__name=city_name)
        data = utils.get_city_weather_dict(weather)
        return data
    except Weather.DoesNotExist:
        return None


def home(request):
    data = {}
    return render(request, "index.html", data)


@require_POST
def add_weather(request):
    city_name = request.POST.get("city")

    city_name = city_name.strip().title()
    if city_name == "":
        messages.error(request, "City name is empty")
        return redirect("weather:home")
    context_db = get_city_weather_from_db(city_name)
    
    context_api = {}
    if context_db is None:
        # call the api
        print("calling the API")
        data_api = utils.get_city_weather(city_name)
        if data_api is not None:
            city_json, weather_json = data_api

            city = City.objects.create(**city_json)

            # add the city object to the weather json
            weather_json["city"] = city
            weather = Weather.objects.create(**weather_json)

            city.save()
            weather.save()
            context_api =  {**city_json, **weather_json}
        else:
            return HttpResponse(
                """<h4 style="color: red;">Unable to reach Weather data provider. Ensure you have internet connection.</h4>"""
            )
    else:
        print("weather data loaded from db")
    
    context = context_db or context_api
    html = render_block_to_string("index.html", 'weather', context)
    return HttpResponse(html)
    # return render(request, "index.html", data_db)


def display_weather(request, data):
    return HttpResponseRedirect(reverse("weather:home"), data=data)
