from tkinter import *
from clock import *
from weather import *
from gallery import *
from appbar import *
#from camera_canvas import *

class Desktop(Canvas):
	def __init__(self, master=None):
		Canvas.__init__(self, master, bd=0, highlightthickness=0, background="white")
		#CameraCanvas.__init__(self, master)
		self.wallpaper = PhotoImage(file="./res/desktop/wallpaper2.png")
		self.create_image(0, 0, anchor="nw", image=self.wallpaper)
		self.init_components()
		self.pack(fill="both", expand=True)
		self.update()

	def init_components(self):
		self.clock = Clock(self, background="black", bd=0, highlightthickness=0)
		self.clock.init_components()
		self.clock.pack(expand=1)
		self.clock.make_draggable()
		self.clock.update()

		self.weather = Weather(self, background="black", bd=0, highlightthickness=0)
		self.weather.init_components()
		self.weather.pack(expand=1)
		self.weather.make_draggable()
		self.weather.update()

		self.appbar = appbar(self, background="black", bd=0, highlightthickness=0)
		self.appbar.init_components()
		self.appbar.pack(expand=1)
		self.appbar.make_draggable()
		#Following lines in def are for testing gallery
		#self.gallery = Toplevel(bg="black")
		#self.gallery.attributes("-fullscreen", False)
		#self.gallery.wm_attributes("-topmost", 1)
		#self.gallery.gallery = gallery(master=self.gallery)
		#self.gallery.geometry("1920x1080")

	def save_location_and_quit(self, event):
		print(self.clock.winfo_x())
		self.destroy()

root = Tk()
root.attributes("-fullscreen", False)
root["background"] = "black"

desktop = Desktop(master=root)
desktop.bind("<Button-3>",desktop.save_location_and_quit)
desktop.mainloop()

root.mainloop() 
