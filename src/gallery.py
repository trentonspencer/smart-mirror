from tkinter import *
import os
import math
from PIL import Image, ImageTk
class gallery(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master, width=1920, height=1080, bd=2, highlightthickness=0, background="black")
		self.label = Label(self, bg="black", foreground="white", font=("mono", 24, "bold"), text="Gallery")
		self.label.pack(anchor="n")
		self.pack(fill=BOTH, expand=True)


		self.gallery_canvas = Canvas(self, width=1920, height=1080, background="black", bd=0, highlightthickness=0)
		self.gallery_canvas.pack(anchor="w", fill=BOTH, expand=1, side=LEFT)
		self.gallery_canvas.grid_rowconfigure(0, weight=1)
		self.gallery_canvas.grid_columnconfigure(0, weight=1)
		numberofrows = math.ceil(len(os.listdir("./res/gallery/"))/3)
		self.gallery_frame = Frame(self.gallery_canvas, background="black")
		self.gallery_canvas.create_window((0,0),window=self.gallery_frame, anchor='w', width=960, height=155*numberofrows)
		self.scrollbar = Scrollbar(self.gallery_canvas)
		self.scrollbar.grid(row=0, column=0, sticky=N+W+S)
		self.gallery_canvas.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command = self.gallery_canvas.yview)



		#self.openimage_canvas.pack(anchor="e", side=RIGHT)
		# self.photo = Image.open("./res/gallery/thisissand.png")
		# self.photo = self.photo.resize((128, 64), Image.ANTIALIAS)
		# self.image = ImageTk.PhotoImage(self.photo)
		# self.create_photo = Label(self.gallery_frame, image=self.image, height = 64, width = 128, background="black")
		# self.create_photo2 = Label(self.gallery_frame, image=self.image, height = 64, width = 128, background="black")
		# self.create_photo.grid(row=0, column=0)
		# self.create_photo2.grid(row=0, column=1)
		# self.create_photo.image = self.image

		cols = 3
		x = 0
		y = 0

		test_listdir = ["thisissand.png"]*10
		for filename in os.listdir("./res/gallery/"):
			photo = Image.open("./res/gallery/" + filename)
			thumbnail = ImageTk.PhotoImage(photo.resize((280, 155), Image.ANTIALIAS))
			label = Label(self.gallery_frame, image=thumbnail, height=155, width=280, background="black", bd=0, highlightthickness=0)
			label.thumbnail = thumbnail
			label.image=filename
			label.bind("<Button-1>", self.openimage)
			label.grid(row=y, column=x)

			x = x+1
			if x >= cols:
				x = 0
				y = y+1

		self.gallery_canvas.config(scrollregion=self.gallery_canvas.bbox(ALL))

	def openimage(self, event):
		print(event.widget.image)
		self.openimage_canvas = Toplevel(Canvas(self, width=1920, height=1080, background="black", bd=0, highlightthickness=0), bg="black")
		photo = Image.open("./res/gallery/" + event.widget.image)
		image = ImageTk.PhotoImage(photo.resize((1920, 1080), Image.ANTIALIAS))
		label = Label(self.openimage_canvas, image=image, height=1080, width=1920, background="black", bd=0, highlightthickness=0)
		label.image = image
		label.grid(row=0, column=0)
		self.openimage_canvas.attributes("-fullscreen", True)
		self.openimage_canvas.wm_attributes("-topmost", 1)
		label.bind("<Button-3>", self.destroyimage)

	def destroyimage(self, event):
		self.openimage_canvas.destroy()
