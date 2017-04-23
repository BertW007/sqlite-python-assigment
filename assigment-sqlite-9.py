#Program name: SQLITE-PYTHON

#Import the sqlite3 module
import sqlite3
#Importing the module tabulate to display the table with columnnames.
from tabulate import tabulate
def main():
	#User input
	print('Please choose the ID and data you want to change:')
	user_input = (
	 	input('Id: '),
	 	input('Name: '),
	 	input('Email: '),
	 	input('Address: '),
		input('City: ')
	 	)
	#This will shift the sequence 'N' number of times to the left
	#http://stackoverflow.com/questions/2150108/
	#efficient-way-to-shift-a-list-in-python
	def shiftIndex(seq, n):
		return seq[n:] + seq[:n]
	# Use the module to create a database or connect to an existing database
	conn = sqlite3.connect('sqliteProject')
	#This function will update the table with new data
	def updateTable():
		with conn:
			#This statement will update the table.
			#Because of the sequence order the shiftIndex function has been used to shift the order 1 time to the left
			conn.execute('''UPDATE customerTable SET
				Name = ?,
				Email = ?,
				Address = ?,
				City = ? WHERE
				Id = ? ''',
				shiftIndex(user_input, 1))
	def retrieveTable():
		with conn:
			#This statement will select all the data from the table customerTable
			cur = conn.cursor()
			cur.execute('SELECT * FROM customerTable')
			#This statement will print the table with tablename and coloumnnames by using the module, tabulate
			rows = cur.fetchall()
			coloumnnames = [''''Id',
			'Name',
			'Email',
			'Address',
			'City''']
			print(' ' * 20, 'customerTable:')
			print(tabulate(rows, headers = coloumnnames))
	updateTable()
	retrieveTable()
	conn.close()
main()
