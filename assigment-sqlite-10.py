import sqlite3
#module tabulate to display the table with columnnames
from tabulate import tabulate
import tkinter
from tkinter import *
from tkinter import messagebox

class GUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.main_window.geometry('700x500')
		self.main_window.wm_title("SQLite Program")

		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

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

		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

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
