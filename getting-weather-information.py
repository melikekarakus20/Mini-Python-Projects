import requests
from pprint import pprint


API_Key = '8281b87c0909efc4c5b2382f21c2b3ed'

city = input("Enter a city:  ")

base_url = "https://home.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
