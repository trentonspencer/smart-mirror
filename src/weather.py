import secrets
from Requestweather import *
from widget import *

class Weather(Widget):
	pass

	def init_components(self):
		self.request = Requestweather()
		self.label_temp = Label(self, bg="black", foreground="white", font=("mono", 64, "bold"), justify="left")
		self.label_temp.pack(anchor="n")
		self.label_weather = Label(self,bg="black", foreground="white", font=("mono", 24, "bold"), justify="left")
		self.label_weather.pack(anchor="sw")
		#self.label_humidity = Label(self,bg="black", foreground="white", font=("mono", 24, "bold"), justify="left")
		#self.label_humidity.pack(anchor="e")
		self.iconcheck = None

	def update(self):
		self.request.requestdata()

		if self.label_temp["text"] != self.request.temp or self.label_weather["text"] != self.request.weather:
			self.label_temp.config(text=self.request.temp+"°")
			self.label_weather.config(text=self.request.weather)
			#self.label_humidity.config(text="humidity:"+""+str(self.request.humidity))

		if self.iconcheck != self.request.icon:
			self.request.requesticon(self.request.icon)
			self.iconcheck = self.request.icon
			self.weatherimage = PhotoImage(data=self.request.iconimage)
			self.create_image(0, 0, anchor="nw", image=self.weatherimage)

		self.after(180000,self.update)

#request = Weather()
#print(request.temp)
#print(secrets.keys["WEATHER_APIKEY"])
