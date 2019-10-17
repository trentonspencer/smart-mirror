import requests
import secrets 
class Requestweather:
    def __init__(self):
        self.response = requests.get('https://api.openweathermap.org/data/2.5/weather?id='+secrets.keys["WEATHER_CITYID"]+'&APPID='+secrets.keys["WEATHER_APIKEY"]+"&units=imperial")
        self.json = self.response.json()
        self.temp = str(self.json['main']['temp'])
        self.weather = self.json['weather'][0]['main']
        self.description = self.json['weather'][0]['description']
        self.humidity = self.json['main']['humidity']
        self.town = self.json['name']
        self.windspeed = self.json['wind']['speed']
        self.winddeg = self.json['wind']['deg']

