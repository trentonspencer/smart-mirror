from tkinter import *
from clock import *

class Desktop(Canvas):
	def __init__(self, master=None):
		Canvas.__init__(self, master, bd=0, highlightthickness=0, background="white")
		self.wallpaper = PhotoImage(file="./res/desktop/wallpaper.png")
		self.create_image(0, 0, anchor="nw", image=self.wallpaper)

		self.init_components()
		self.pack(fill="both", expand=True)

	def init_components(self):
		self.clock = Clock(self, background="black")
		self.clock.init_components()
		self.clock.pack(expand=1)
		self.clock.make_draggable()
		self.clock.update()

root = Tk()
root.attributes("-fullscreen", False)
root["background"] = "black"

desktop = Desktop(master=root)
desktop.mainloop()

root.mainloop()
