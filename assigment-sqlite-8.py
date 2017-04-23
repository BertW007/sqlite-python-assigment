#Program name: SQLITE-PYTHON

#Import the sqlite3 module
import sqlite3
#Importing the module tabulate to display the table with columnnames.
from tabulate import tabulate

def main():
	# Use the module to create a database or connect to an existing database.
	conn = sqlite3.connect('sqliteProject')
	#Insert data  into the database.
	customer = (
		(1, 'Per', 'pda@eal.dk', 'Mystreet 1', 'Odense'),
		(2, 'Arthur', 'at@hotmail.com', 'Allstreet 741','Vilnius'),
		(3, 'Alice', 'ab@gmail.com', 'Topstreet 56', 'London'))
	#Defining the function for creating a table.
	def createTable():
		#This will delete the table, if it exits.
		#Then it will create a new table with the columns.
		conn.execute('''DROP TABLE IF EXISTS customerTable''')
		conn.execute('''CREATE TABLE customerTable
			(Id INT PRIMARY KEY,
			Name TEXT,
			Email TEXT,
			Address TEXT,
			City TEXT); ''')
		#This will insert the data into the table
		conn.executemany('''INSERT INTO customerTable VALUES
			(?, ?, ?, ?, ?)''',
			customer)
	#Define the function, which will show the database
	def retrieveTable():
		#With this you do not need a conn.commit. Changes will be automatically saved.
		with conn:
			#This statement will select all the data from the table customerTable.
			cur = conn.cursor()
			cur.execute('SELECT * FROM customerTable')
			#This statement will print the table with tablename and columnnames by using the module, tabulate
			rows = cur.fetchall()
			columnnames = ['''Id',
			'Name',
			'Email',
			'Address',
			'City''']
			print(' ' * 20, 'customerTable:')
			print(tabulate(rows, headers = columnnames))
	#Call the two functions, createTable() and retrieveTable()
	createTable()
	retrieveTable()
	#Close the connection to the databse
	conn.close()
#Call the function, main()
main()
