from tkinter import *
from abc import ABC, abstractmethod

class Widget(Canvas, ABC):
	pass

	@abstractmethod
	def init_components(self):
		pass

	@abstractmethod
	def update(self):
		pass

	def make_draggable(self):
		self._drag_component = Canvas(self, bg="white", bd=0, highlightthickness=0, height=16)
		self._drag_component.pack(fill="x")
		self._drag_component.bind("<Button-1>", Widget.on_start_drag)
		self._drag_component.bind("<B1-Motion>", Widget.on_dragged)

	@staticmethod
	def on_start_drag(event):
		component = event.widget
		widget = component.master
		component._start_x = event.x
		component._start_y = event.y

	@staticmethod
	def on_dragged(event):
		component = event.widget
		widget = component.master

		x = widget.winfo_x() + (event.x - component._start_x)
		y = widget.winfo_y() + (event.y - component._start_y)

		width = widget.winfo_width()
		height = widget.winfo_height()

		m_width = widget.master.winfo_width()
		m_height = widget.master.winfo_height()

		if x < 0:
			x = 0
		elif x+width > m_width:
			x = m_width-width

		if y < 0:
			y = 0
		elif y+height > m_height:
			y = m_height-height

		widget.place(x=x, y=y)
