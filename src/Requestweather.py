import requests
import secrets, base64
class Requestweather:
	def __init__ (self):
		self.temp = ''
		self.weather = ''
		self.description = ''
		self.humidity = ''
		self.town = ''
		self.windspeed = ''
		self.winddeg = ''
		self.icon = None
	def requestdata(self):
		self.response = requests.get('https://api.openweathermap.org/data/2.5/weather?id='+secrets.keys["WEATHER_CITYID"]+'&APPID='+secrets.keys["WEATHER_APIKEY"]+"&units=imperial")
		self.json = self.response.json()
		if self.json:
			if 'name' in self.json:
				self.town = self.json['name']
			if 'main' in self.json:
				main = self.json['main']
				if 'temp' in main:
					self.temp = str(int(main['temp']))
				if 'humidity' in main:
					self.humidity = main['humidity']
			if 'weather' in self.json:
				weather = self.json['weather'][0]
				if 'main' in weather:
					self.weather = weather['main']
				if 'description' in weather:
					self.description = weather['description']
				if 'icon' in weather:
					self.icon = weather['icon']
			if 'wind' in self.json:
				wind = self.json['wind']
				if 'speed' in wind:
					self.windspeed = wind['speed']
				if 'deg' in wind:
					self.winddeg = wind['deg']
			


		# self.response = requests.get('https://api.openweathermap.org/data/2.5/weather?id='+secrets.keys["WEATHER_CITYID"]+'&APPID='+secrets.keys["WEATHER_APIKEY"]+"&units=imperial")
		# self.json = self.response.json()
		# self.temp = str(int(self.json['main']['temp'])) if self.json['main']['temp'] else ''
		# self.weather = self.json['weather'][0]['main'] if self.json['weather'][0]['main'] else ''
		# self.description = self.json['weather'][0]['description'] if self.json['weather'][0]['description'] else ''
		# self.humidity = self.json['main']['humidity'] if self.json['main']['humidity'] else ''
		# self.town = self.json['name'] if self.json['name'] else ''
		# self.windspeed = self.json['wind']['speed'] if self.json['wind']['speed'] else ''
		# self.winddeg = self.json['wind']['deg'] if self.json['wind']['deg'] else ''
		# self.icon = self.json['weather'][0]['icon'] if self.json['weather'][0]['icon'] else '' 
	def requesticon(self, icon):
		iconurl = ('http://openweathermap.org/img/wn/'+icon+'@2x.png')
		#print(iconurl)
		response = requests.get(iconurl, stream = True)
		#print(response.status_code)
		self.iconimage = base64.encodebytes(response.raw.read())
		#print(self.iconimage)
	#def geticon(self):
		

