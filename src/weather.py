import secrets
from Requestweather import *
from widget import *

class Weather(Widget):
	pass

	def init_components(self):
		self.request = Requestweather()
		self.label1 = Label(self, bg="black", foreground="white", font=("mono", 32, "bold"),text=self.request.temp+'°')
		self.label1.pack(anchor=N)
		self.label2 = Label(self,bg="black", foreground="white", font=("mono", 24, "bold"),text=self.request.description)
		self.label2.pack(anchor=SE)
		self.weatherimage = PhotoImage(data=self.request.iconimage)
		print(self.request.iconimage)
		self.create_image(0, 0, anchor="nw", image=self.weatherimage)
		
	def update(self):
		pass
	
#request = Weather()
#print(request.temp)
#print(secrets.keys["WEATHER_APIKEY"])
