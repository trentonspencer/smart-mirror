from tkinter import *
import os
from PIL import Image, ImageTk
class gallery(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master, width=1920, height=1080, bd=2, highlightthickness=0, background="black")
		self.label = Label(self, bg="black", foreground="white", font=("mono", 24, "bold"), text="Gallery")
		self.label.pack(anchor="n")
		self.pack()
		self.gallery_frame= Frame(self, width=960, height=540, background="black")
		self.gallery_frame.pack(anchor="w", fill=X, expand=1, side=LEFT)
		# self.photo = Image.open("./res/gallery/thisissand.png")
		# self.photo = self.photo.resize((128, 64), Image.ANTIALIAS)
		# self.image = ImageTk.PhotoImage(self.photo)
		# self.create_photo = Label(self.gallery_frame, image=self.image, height = 64, width = 128, background="black")
		# self.create_photo2 = Label(self.gallery_frame, image=self.image, height = 64, width = 128, background="black")
		# self.create_photo.grid(row=0, column=0)
		# self.create_photo2.grid(row=0, column=1)
		# self.create_photo.image = self.image

		cols = 6
		x = 0
		y = 0

		test_listdir = ["thisissand.png"]*10
		for filename in test_listdir: #os.listdir("./res/gallery/"):
			photo = Image.open("./res/gallery/" + filename)
			thumbnail = ImageTk.PhotoImage(photo.resize((128, 64), Image.ANTIALIAS))
			label = Label(self.gallery_frame, image=thumbnail, height=64, width=128, background="black")
			label.thumbnail = thumbnail
			label.grid(row=y, column=x)

			x = x+1
			if x >= cols:
				x = 0
				y = y+1
