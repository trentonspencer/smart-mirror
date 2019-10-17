import requests
import secrets, base64
class Requestweather:
    pass
    def requestdata(self):
        self.response = requests.get('https://api.openweathermap.org/data/2.5/weather?id='+secrets.keys["WEATHER_CITYID"]+'&APPID='+secrets.keys["WEATHER_APIKEY"]+"&units=imperial")
        self.json = self.response.json()
        self.temp = str(int(self.json['main']['temp']))
        self.weather = self.json['weather'][0]['main']
        self.description = self.json['weather'][0]['description']
        self.humidity = self.json['main']['humidity']
        self.town = self.json['name']
        self.windspeed = self.json['wind']['speed']
        #self.winddeg = self.json['wind']['deg']
        self.icon = self.json['weather'][0]['icon']
    def requesticon(self, icon):
        iconurl = ('http://openweathermap.org/img/wn/'+icon+'@2x.png')
        #print(iconurl)
        response = requests.get(iconurl, stream = True)
        #print(response.status_code)
        self.iconimage = base64.encodebytes(response.raw.read())
        #print(self.iconimage)
    #def geticon(self):
        

