from django.contrib import messages
from django.forms import URLInput
from django.shortcuts import render
import json
import urllib.request

import requests
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # res = urllib.request.urlopen(
        #     'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=52e9cfd5f67b3c712f0940dec40df181').read()
        # json_data = json.loads(res)

        res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' +
                           city + '&appid=52e9cfd5f67b3c712f0940dec40df181').json()

        if res['cod'] == 200:
            # change to a dictionary
            data = {
                "country_code": res['sys']['country'],
                "coordinate": str(res['coord']['lon']) + ' ' + str(res['coord']['lat']),
                "temp": str(round(1.8 * (res['main']['temp'] - 273) + 32, 2)) + ' °F',
                "pressure": str(res['main']['pressure']) + " atm",
                "humidity": str(res['main']['humidity']) + " %",
                "weather": res['weather'][0],

            }
        else:
            data = {
                "country_code": '',
                "coordinate": '',
                "temp": '',
                "pressure": '',
                "humidity": '',
                "weather": '',

            }
            messages.info(
                request, "Oops!! That city does not exist in the world!")

    # very common error will occur
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {"city": city, "data": data})
