from tkinter import *
import os

class gallery(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master, bd=0, highlightthickness=0, background="black")
		self.label = Label(self, bg="black", foreground="white", font=("mono", 24, "bold"), text = 'Gallery')
		self.label.pack(anchor='n')
		self.pack()
