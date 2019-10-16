import datetime
from widget import *

class Clock(Widget):
	pass

	def init_components(self):
		self.label = Label(self, bg="black", foreground="white", font=("mono", 32, "bold"), text="test")
		self.label.pack(expand=1)

	def update(self):
		time = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
		if self.label["text"] != time:
			self.label.config(text=time)

		self.after(200, self.update)
