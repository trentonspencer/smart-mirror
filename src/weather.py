import secrets
from Requestweather import *
from widget import *

class Weather(Widget):
	pass

	def init_components(self):
		self.request = Requestweather()
		self.label1 = Label(self, bg="black", foreground="white", font=("mono", 32, "bold"),text=self.request.temp+'°')
		self.label1.pack(anchor=W)
		
	def update(self):
		pass
	
#request = Weather()
#print(request.temp)
#print(secrets.keys["WEATHER_APIKEY"])
