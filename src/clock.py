import datetime
from widget import *

class Clock(Widget):
	pass

	def init_components(self):
		self.time_label = Label(self, bg="black", foreground="white", font=("mono", 64, "bold"), justify="left")
		self.time_label.pack(anchor="w")
		self.date_label = Label(self, bg="black", foreground="white", font=("mono", 18, "bold"), justify="left")
		self.date_label.pack(anchor="w")

	def update(self):
		time = datetime.datetime.now().strftime("%I:%M%p")
		date = datetime.datetime.now().strftime("%A\n%b %d, %Y")
		if self.time_label["text"] != time:
			self.time_label.config(text=time)

		if self.date_label["text"] != time:
			self.date_label.config(text=date)

		self.after(200, self.update)
