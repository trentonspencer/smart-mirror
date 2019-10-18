import secrets
from Requestweather import *
from widget import *

class Weather(Widget):
	pass

	def init_components(self):
		self.request = Requestweather()
		self.label1 = Label(self, bg="black", foreground="white", font=("mono", 32, "bold"))
		self.label1.pack(anchor=N)
		self.label2 = Label(self,bg="black", foreground="white", font=("mono", 24, "bold"))
		self.label2.pack(anchor=S)
		self.iconcheck = None
		
	def update(self):
		self.request.requestdata()
		print(self.request.temp)
		if self.label1["text"] != self.request.temp or self.label2["text"] != self.request.description:
			self.label1.config(text=self.request.temp+'°')
			self.label2.config(text=self.request.description)
		if self.iconcheck != self.request.icon:
			self.request.requesticon(self.request.icon)
			self.iconcheck = self.request.icon 
			self.weatherimage = PhotoImage(data=self.request.iconimage)
			self.create_image(0, 0, anchor="nw", image=self.weatherimage)
		self.after(180000,self.update)
	
#request = Weather()
#print(request.temp)
#print(secrets.keys["WEATHER_APIKEY"])
