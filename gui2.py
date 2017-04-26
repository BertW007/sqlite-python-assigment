import tkinter
from tkinter import *
import tkinter as tk
import sqlite3
from tabulate import tabulate

class MainGui():
	def __init__(self):
		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('650x500')

		#Set Window Title
		self.main_window.wm_title("SQL Program")

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window, width=600, height=200)

		#Variables that are user input
		self.idCust = tkinter.StringVar()
		self.name = tkinter.StringVar()
		self.email = tkinter.StringVar()
		self.address= tkinter.StringVar()
		self.city = tkinter.StringVar()


		#Setting labels and entry widget for the
		#different user inputs
		#Setting default entries
		self.idCust_label = tkinter.Label\
		(self.top_frame, text="idCust:")\
		.grid(row=0,column=0)

		self.idCust_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.idCust_entry.grid(row=0, column=1)

		self.name_label = tkinter.Label\
		(self.top_frame, text="Name:")\
		.grid(row=1, column=0)

		self.name_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.name_entry.grid(row=1, column=1)

		self.email_label = tkinter.Label\
		(self.top_frame, text="Email:")\
		.grid(row=2,column=0)

		self.email_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.email_entry.grid(row=2,column=1)

		self.address_label = tkinter.Label\
		(self.top_frame, text="Address:")\
		.grid(row=3,column=0)

		self.address_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.address_entry.grid(row=3,column=1)

		self.city_label = tkinter.Label\
		(self.top_frame, text="City:")\
		.grid(row=4,column=0)

		self.city_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.city_entry.grid(row=4,column=1)

		# create a Text widget
		self.txt = tk.Text(self.bottom_frame, borderwidth=3, relief="sunken")
		self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)


		# create a Scrollbar and associate it with txt
		self.scrollb = tk.Scrollbar(self.bottom_frame, command=self.txt.yview)
		self.scrollb.grid(row=0, column=1, sticky='nsew')
		self.txt['yscrollcommand'] = self.scrollb.set

		#Sets the button widgets

		self.insert_button = tkinter.Button\
		(self.middle_frame, text="Insert",\
			command=self.insert)\
		.grid(row=0,column=0, pady=50)

		self.insert_button = tkinter.Button\
		(self.middle_frame, text="Show",\
			command=self.show)\
		.grid(row=0,column=1, pady=50)

		self.search_button = tkinter.Button\
		(self.middle_frame, text="Search",\
			command=self.search)\
		.grid(row=0,column=4, pady=50)

		self.quit_button = tkinter.Button\
		(self.middle_frame, text="Quit", \
			command=self.main_window.destroy)\
		.grid(row=0,column=6, pady=50)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		self.bottom_frame.grid_propagate(False)
		self.bottom_frame.grid_rowconfigure(0, weight=1)
		self.bottom_frame.grid_columnconfigure(0, weight=1)

		#Enter the tkinter main loop.
		tkinter.mainloop()


	def insert(self):
		idCust = int(self.idCust_entry.get())
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
			#https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
			cur.execute("SELECT * FROM "+tableName)
			columnNames = list(map(lambda x: x[0], cur.description))

			#Gets the data from the table
			cur.execute("SELECT * FROM "+tableName)
			data = (cur.fetchall())

			#Uses tabulate to output the database table like a table in the console
			tableData = tabulate(data, headers=columnNames,tablefmt='orgtbl')
		text = self.txt
		text.delete('1.0', END)
		text.insert(INSERT, str(tableData+'\n'))

	def search(self):
		data = ''

		idCust = self.idCust_entry.get()
		name = self.name_entry.get()
		email = self.email_entry.get()
		address = self.address_entry.get()
		city = self.city_entry.get()

		inputList =[idCust,name,email,address,city]

		with con:
			cur = con.cursor()

			cur.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
			tableName = cur.fetchall()[0][1]

			cur.execute("SELECT * FROM "+tableName)
			columnNames = list(map(lambda x: x[0], cur.description))

			x=0
			for column in inputList:
				if column != '':
					t = (column,)
					cur.execute('SELECT * FROM customerTable WHERE '+columnNames[x]+'=?', t)
					data = [cur.fetchone()]
				x+=1

			else:
				pass
			# print(name)
			# con.execute('''SELECT * FROM customerTable WHERE Id='2' ''')
			# data = cur.fetchone()

			# #Uses tabulate to output the database table like a table in the console
			tableData = tabulate(data, headers=columnNames,tablefmt='orgtbl')

		text = self.txt
		text.delete('1.0', END)
		text.insert(INSERT, str(tableData+'\n'))



con = sqlite3.connect('test.db')
gui = MainGui()
