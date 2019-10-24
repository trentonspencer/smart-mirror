from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image as Img
from PIL import ImageTk
from tkinter import *
from widget import *

class CameraCanvas(Widget):
	def __init__(self, master):
		Widget.__init__(self, master, width=1920, height=1080, bg="red")
		self.pack(expand=1)
		print(self.winfo_width(), self.winfo_height())
		self.camera = PiCamera()
		self.camera.resolution = (1920, 1080)
		self.camera.framerate = 32
		self.rawCapture = PiRGBArray(self.camera, size=(1920, 1080))

	def init_components(self):
		print('ok')

	def update(self):
		frames = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
		for frame in frames:
			image = frame.array

			image = Img.fromarray(image)
			self.image = ImageTk.PhotoImage(image)
			self.create_image(0, 0, anchor="nw", image=self.image)

			self.rawCapture.truncate(0)
			break

		self.after(32, self.update)

