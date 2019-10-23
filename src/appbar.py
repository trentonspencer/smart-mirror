from gallery import *
from widget import *
import os
from PIL import Image, ImageTk
class appbar(Widget):
	def update(self):
		pass

	def init_components(self):
		gallery_photo = Image.open("./res/AppIcons/gallery.png")
		gallery_thumbnail = ImageTk.PhotoImage(gallery_photo.resize((64, 64), Image.ANTIALIAS))
		gallery_label = Label(self, image=gallery_thumbnail, height=64, width=64, background="black", bd=0, highlightthickness=0)
		gallery_label.thumbnail = gallery_thumbnail
		gallery_label.pack()
		gallery_label.bind("<Button-1>", self.build_gallery)


	def build_gallery(self, event):
		self.gallery = Toplevel(bg="black")
		self.gallery.attributes("-fullscreen", True)
		self.gallery.wm_attributes("-topmost", 1)
		self.gallery.gallery = gallery(master=self.gallery)
		self.gallery.geometry("1920x1080")
		self.gallery.bind("<Button-3>", self.destroy_window)

	def destroy_window(self, event):
		self.gallery.destroy()
