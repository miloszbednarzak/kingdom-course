import os

import requests  # tą bibliotekę trzeba doinstalować
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]

def check_temperature(szerokosc, wysokosc):
    params = {  # to są parametry które przekazujemy do API
        "lat": szerokosc,
        "lon": wysokosc,
        "units": "metric",
        "appid": api_key
    }

    # to jest url naszego API:
    url = "https://api.openweathermap.org/data/2.5/weather"

    # w ten sposób wywołujemy zawołanie do API:
    response = requests.get(url, params=params)

    json_ = response.json()

    # z całości odpowiedzi naszego api chcemy tylko informację jaka jest temperatura:

    return json_["main"]["temp"]


if __name__ == '__main__':
    # jak chcecie sprawdzić czy Wasze połączene z API działa to odpalcie to:
    weather_forecast = check_temperature(80, 93)
    print(weather_forecast)
