import sqlite3
#module tabulate to display the table with columnnames
from tabulate import tabulate
import tkinter
from tkinter import *
<<<<<<< HEAD
import tkinter as tk
import sqlite3
from tabulate import tabulate
=======
from tkinter import messagebox
>>>>>>> ef62ff5ce705d1d9ee032c636173799d2fa271bb

class GUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.main_window.geometry('700x500')
		self.main_window.wm_title("SQLite Program")

<<<<<<< HEAD
		#Set Window Default Size
		self.main_window.geometry('600x500')

		#Set Window Title
		self.main_window.wm_title('SQLite Control Program')

		#Creating the three frames
=======
>>>>>>> ef62ff5ce705d1d9ee032c636173799d2fa271bb
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

<<<<<<< HEAD
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
=======
		self.Id = tkinter.IntVar()
		self.Name = tkinter.StringVar()
		self.Email = tkinter.StringVar()
		self.Address = tkinter.StringVar()
		self.City = tkinter.StringVar()

		#Sets the label\entry widgets - ID
		self.Id = tkinter.Label(self.top_frame, text="Id:").grid(row=0,column=0)
		self.Id_entry = tkinter.Entry(self.top_frame, bd =5)
		self.Id_entry.grid(row=0, column=1)

		#Sets the label\entry widgets - NAME
		self.Name_label = tkinter.Label(self.top_frame, text="Name:").grid(row=1, column=0)
		self.Name_entry = tkinter.Entry(self.top_frame, bd =5)
		self.Name_entry.grid(row=1, column=1)

		#Sets the label\entry widgets - EMAIL
		self.Email_label = tkinter.Label(self.top_frame, text="Email:").grid(row=2,column=0)
		self.Email_entry = tkinter.Entry(self.top_frame, bd =5)
		self.Email_entry.grid(row=2,column=1)

		#Sets the label\entry widgets - Address
		self.Address_label = tkinter.Label(self.top_frame, text="Address:").grid(row=3,column=0)
		self.Address_entry = tkinter.Entry(self.top_frame, bd =5)
		self.Address_entry.grid(row=3,column=1)

		#Sets the label\entry widgets - CITT
		self.City_label = tkinter.Label(self.top_frame, text="City:").grid(row=4,column=0)
		self.City_entry = tkinter.Entry(self.top_frame, bd =5)
		self.City_entry.grid(row=4,column=1)

		#Sets the label\button widgets
		self.clear_button = tkinter.Button(self.middle_frame, text="Clear Entry",command=self.clearEntry).grid(row=0,column=0, pady=50)
		self.insert_button = tkinter.Button(self.middle_frame, text="Insert",command=self.insertData).grid(row=0,column=1, pady=50)
		self.update_button = tkinter.Button(self.middle_frame, text="Update",command=self.updateTable).grid(row=0,column=2, pady=50)
		self.delete_button = tkinter.Button(self.middle_frame, text="Delete",command=self.deleteRow).grid(row=0,column=3, pady=50)
		self.show_button = tkinter.Button(self.middle_frame, text="Show",command=self.showTable).grid(row=0,column=4, pady=50)
		self.help_button = tkinter.Button(self.middle_frame, text="Help",command=self.programHelp).grid(row=0,column=5, pady=50)
		self.close_button = tkinter.Button(self.middle_frame, text="Quit",command=self.closeDatabase).grid(row=0,column=6, pady=50)

		#Sets the text widget - DISPLAY DATA
		self.text = tkinter.Text(self.bottom_frame)
		#Sets scroll
		scroll=tkinter.Scrollbar(self.bottom_frame, command=self.text.yview)
		self.text.configure(yscrollcommand=scroll.set)

		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT, fill=Y)
>>>>>>> ef62ff5ce705d1d9ee032c636173799d2fa271bb

		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

<<<<<<< HEAD
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
=======
	def clearEntry(self):

		#Deletes the text in the entry boxes
		self.Id_entry.delete(0, END)
		self.Name_entry.delete(0, END)
		self.Email_entry.delete(0, END)
		self.Address_entry.delete(0, END)
		self.City_entry.delete(0, END)

	def insertData(self):
		uId = self.Id_entry.get()
		uName = self.Name_entry.get()
		uEmail = self.Email_entry.get()
		uAddress = self.Address_entry.get()
		uCity = self.City_entry.get()

		customer = (
			uId, uName, uEmail, uAddress, uCity)
		conn.execute('''INSERT INTO customerTable VALUES
			(?, ?, ?, ?, ?)''',
			customer)

	def updateTable(self):

		#With this you do not need a conn.commit
		#The changes will be automatically saved
		with conn:
			uId = self.Id_entry.get()
			uName = self.Name_entry.get()
			uEmail = self.Email_entry.get()
			uAddress = self.Address_entry.get()
			uCity = self.City_entry.get()
			customer = (
				uName, uEmail, uAddress, uCity, uId)
			conn.execute('''UPDATE customerTable SET
				Name = ?,
				Email = ?,
				Address = ?,
				City = ? WHERE
				Id = ? ''',
				customer)

	def deleteRow(self):
		with conn:
			uId = self.Id_entry.get()
			uName = self.Name_entry.get()
			uEmail = self.Email_entry.get()
			uAddress = self.Address_entry.get()
			uCity = self.City_entry.get()
			customer = (
				uId, uName, uEmail, uAddress, uCity)
			conn.execute('''DELETE FROM customerTable
				WHERE Id = ? or Name = ? or\
				 Email = ? or\
				  Address = ? or\
				   City = ?''',
				customer)
	def showTable(self):
		with conn:
			cur = conn.cursor()
			cur.execute('SELECT * FROM customerTable')
			rows = cur.fetchall()
			columnnames = [
			'Id',
			'Name',
			'Email',
			'Address',
			'City']
			self.text.delete('1.0', END)
			self.text.insert(INSERT, tabulate\
				(rows, headers = columnnames)\
				 + '\n\n')
	def programHelp(self):

		dialog_title = 'Entry Information'
		dialog_text = 'In the first entry box you type in the ID which will be to identify which row, you want the data to be input.\n'+'*'*75+'\n'\
		'The second entry box is where you type in the name of the person you want in that specific row. \n'+'*'*75+'\n'\
		'The third entry box is where you type in the email of the person, for that specific row. \n'+'*'*75+'\n'\
		'The fourth entry box is where you type in address of the person, for that specific row. \n'+'*'*75+'\n'\
		'The fifth entry box is where you type in the city for the person for that specific row.'
		messagebox.showinfo(dialog_title, dialog_text)
	def closeDatabase(self):
		conn.close()
		self.main_window.destroy()

#Initiate program
conn = sqlite3.connect('sqliteProject')
myGUI = GUI()
>>>>>>> ef62ff5ce705d1d9ee032c636173799d2fa271bb
