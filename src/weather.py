import secrets
from Requestweather import *
from widget import *
import time
from PIL import Image, ImageTk
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
		self.settings_photo = Image.open("./res/AppIcons/cog.png")
		self.settings_icon = ImageTk.PhotoImage(self.settings_photo.resize((48, 48), Image.ANTIALIAS))
		self.settings_label = Label(self, image=self.settings_icon, height=48, width=48, background="black", bd=0, highlightthickness=0)
		self.settings_icon.thumbnail = self.settings_icon
		self.settings_label.place(x=300, y=0) #Placement works for now, must be changed to be based off of canvas size
		self.settings_label.bind("<Button-1>", self.settings)
	
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

	
	def settings(self, event):
		self.counting = False
		print("Entered Settings")
		self.settings_canvas = Toplevel(Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), background="black", bd=0, highlightthickness=0), bg="black")
		self.settings_canvas.attributes("-fullscreen", True)
		self.settings_canvas.bind("<Button-3>",self.settings_destroy)
		self.enter_town_label = Label(self.settings_canvas, text="Town", font=("mono", 24, "bold"), background="black", foreground="white")
		self.enter_town = Entry(self.settings_canvas)
		self.enter_town_label.grid(row=0, column=0)
		self.enter_town.grid(row=0, column=1)
		#add way to choose what displays

	def settings_destroy(self, event):
		self.settings_canvas.destroy()
#request = Weather()
#print(request.temp)
#print(secrets.keys["WEATHER_APIKEY"])
