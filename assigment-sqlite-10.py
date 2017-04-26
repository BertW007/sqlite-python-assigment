import tkinter
from tkinter import *
import tkinter as tk
import sqlite3
from tabulate import tabulate

class Gui:
	def __init__(self):
		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('600x500')

		#Set Window Title
		self.main_window.wm_title('SQLite Control Program')

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		#Setting Variables
		self.id_entry = tkinter.StringVar()
		self.name_entry = tkinter.StringVar()
		self.email_entry = tkinter.StringVar()
		self.address_entry = tkinter.StringVar()
		self.city_entry = tkinter.StringVar()

		#Sets the label\entry widgets - ID
		self.id_label = tkinter.Label(self.top_frame, text='ID: ').grid(row=0, column=0, sticky=W)
		self.id_entry = tkinter.Entry(self.top_frame, textvariable = self.id_entry, width = 20).grid(row=0, column=1)

		#Sets the label\entry widgets - NAME
		self.name_label = tkinter.Label(self.top_frame, text='Name: ').grid(row=1, column=0, sticky=W)
		self.name_entry = tkinter.Entry(self.top_frame, textvariable = self.name_entry, width = 20).grid(row=1, column=1)

		#Sets the label\entry widgets - E-MAIL
		self.email_name = tkinter.Label(self.top_frame, text='E-mail: ').grid(row=2, column=0, sticky=W)
		self.email_entry = tkinter.Entry(self.top_frame, textvariable = self.email_entry, width = 20).grid(row=2, column=1)

		#Sets the label\entry widgets - ADDRESS
		self.address_label = tkinter.Label(self.top_frame, text='Address: ').grid(row=3, column=0, sticky=W)
		self.address_entry = tkinter.Entry(self.top_frame, textvariable = self.address_entry, width = 20).grid(row=3, column=1)

		#Sets the label\entry widgets - CITY
		self.city_label = tkinter.Label(self.top_frame, text='City: ').grid(row=4, column=0, sticky=W)
		self.city_entry = tkinter.Entry(self.top_frame, textvariable = self.city_entry, width = 20).grid(row=4, column=1)

		#Sets the text widget - DISPLAY DATA
		self.text_window = tk.Text(self.middle_frame, borderwidth=3)
		self.text_window.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

		self.scrollb = tk.Scrollbar(self.middle_frame, command=self.text_window.yview)
		self.scrollb.grid(row=0, column=1, sticky='nsew')
		self.text_window['yscrollcommand'] = self.scrollb.set

		#Sets the button widgets
		self.show_button = tkinter.Button(self.bottom_frame, text='Insert', command=self.insert).grid(row=0, column=0, pady=10)
		self.show_button = tkinter.Button(self.bottom_frame, text='Show', command=self.show).grid(row=0, column=1, pady=10)
		self.help_button = tkinter.Button(self.bottom_frame, text='Help', command=self.help).grid(row=0, column=2, pady=10)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy).grid(row=0, column=3, pady=10)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

		#Function
	def insert(self):
		idCust = int(self.id_entry.get())
		name = self.name_entry.get()
		email = self.email_entry.get()
		address = self.address_entry.get()
		city = self.city_entry.get()

		customer = (
		(idCust, name, email, address, city)
			)

		con.execute('''INSERT INTO customerTable VALUES
			(?, ?, ?, ?, ?)''', customer)

	# The info method is a callback function for
	# the show info button.
	def show(self):
		with con:

			#Gets the table name from the database
			cur = con.cursor()

			cur.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
			tableName = cur.fetchall()[0][1]

			#Gets the column names from the table
			cur.execute("SELECT * FROM "+tableName)
			columnNames = list(map(lambda x: x[0], cur.description))

			#Gets the data from the table
			cur.execute("SELECT * FROM "+tableName)
			data = (cur.fetchall())

			#Uses tabulate to output the database table like a table in the console
			tableData = tabulate(data, headers=columnNames,tablefmt='orgtbl')
		text = self.text_window
		text.delete('1.0', END)
		text.insert(INSERT, str(tableData+'\n'))

	def help(self):
		print("HI!")

#Create connection to DB
con = sqlite3.connect('assigment-sqlite3.db')
#Create object
myGui = Gui()
