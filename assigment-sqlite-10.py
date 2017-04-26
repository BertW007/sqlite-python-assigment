import tkinter
from tkinter import *

class Gui:
	def __init__(self):
		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('400x200')

		#Set Window Title
		self.main_window.wm_title('SQLite Control Program')

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		#Setting Variables
		self.id = tkinter.StringVar()
		self.name = tkinter.StringVar()

		#Sets the label\entry widgets - ID
		self.id_label = tkinter.Label(self.top_frame, text='ID: ').grid(row=0,column=0, sticky=W)
		self.id_entry = tkinter.Entry(self.top_frame, textvariable = self.id).grid(row=0,column=1)

		#Sets the label\entry widgets - NAME
		self.name_label = tkinter.Label(self.top_frame, text='Name: ').grid(row=1,column=0, sticky=W)
		self.name_entry = tkinter.Entry(self.top_frame, textvariable = self.name).grid(row=1,column=1)

		#Sets the label\entry widgets - E-MAIL
		self.email_name = tkinter.Label(self.top_frame, text='E-mail: ').grid(row=2,column=0, sticky=W)
		self.email_entry = tkinter.Entry(self.top_frame, textvariable = self.id).grid(row=2,column=1)

		#Sets the label\entry widgets - ADDRESS
		self.address_label = tkinter.Label(self.top_frame, text='Address: ').grid(row=3,column=0, sticky=W)
		self.address_entry = tkinter.Entry(self.top_frame, textvariable = self.id).grid(row=3,column=1)

		#Sets the label\entry widgets - CITY
		self.city_label = tkinter.Label(self.top_frame, text='City: ').grid(row=4,column=0, sticky=W)
		self.city_entry = tkinter.Entry(self.top_frame, textvariable = self.id).grid(row=4,column=1)

		#Sets the text widget - DISPLAY DATA

		#Sets the label\button widgets
		self.show_button = tkinter.Button(self.bottom_frame, text='Show', command=self.main_window.destroy).grid(row=0,column=0, pady=10)
		self.help_button = tkinter.Button(self.bottom_frame, text='Help', command=self.main_window.destroy).grid(row=0,column=1, pady=10)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy).grid(row=0,column=2, pady=10)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

#Create object
myGui = Gui()
