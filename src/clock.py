import datetime
from widget import *

class Clock(Widget):
	pass

	def init_components(self):
		self.label = Label(self, bg="black", foreground="white", font=("mono", 32, "bold"))
		self.label.pack(expand=1)

	def update(self):
		time = datetime.datetime.now().strftime("%H:%M:%S\n%b %d, %Y ")
		if self.label["text"] != time:
			self.label.config(text=time)

		self.after(200, self.update)
