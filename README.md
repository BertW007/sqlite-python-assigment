# sqlite-python-assigment
#screenshots are to be added

Lillebaelt Academy of 
University of applied sciences


Instructor
Per Dahlstrøm


Author
Lidia Vasileva lidi0168@edu.eal.dk

2017-05-08
Table of Contents
 1. Introduction	1
 2. Download the Code	2
 3. Command Line Shell for SQLite	3
 3.1. Getting Started	3
 I) Starting sqlite3 and creating a database	3
 II) How to exit sqlite3	3
 4. Entering SQL	3
 4.1. CREATE a table, INSERT and SELECT	3
 5. Special dot commands to sqlite3	4
 6. Writing results to a file	4
 7. Recovery	5
 8. How to use SQLite with Python application	5
 9. UPDATE	5
 10. Create a GUI	5
 11. Create a GUI to do full CRUD	5
 12. Test section	5
 13. Student Chapter	5
 13.1. Creating a Web-frame	5


 1.  Introduction
SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.

SQLite is used by literally millions of applications with literally billions and billions of deployments. SQLite is the most widely deployed database engine in the world today. 
Several examples are showed bellow: 

 2.  Download the Code
The machine this project will be held is running Debian 8 (Jessie), which at this time does not come pre-installed with SQLite. 
In a command terminal the following command is executed: 
sudo apt-get install sqlite3

After entering the password, SQLite should be installed on the system. 
 3.  Command Line Shell for SQLite
Sqlite3 allows a user to enter and execute SQL commands against and SQLite database from within
the terminal.
 3.1.  Getting Started
 I)  Starting sqlite3 and creating a database
To  start the SQLite, the following command is executed in the command terminal:
sqlite3
The following screenshot showcases the output.

 II)  How to exit sqlite3
To  exit the SQLite, the following command is executed in the command terminal:
.exit
 4.  Entering SQL
 4.1.  CREATE a table, INSERT and SELECT
To create a table in a database with the required columns the following command is executed:
CREATE TABLE customerTable( idCust integer NOT NULL UNIQUE, name text NOT NULL, email text NOT NULL UNIQUE, address text NOT NULL, city text NOT NULL);

To insert the required information the following command is executed:
INSERT INTO customerTable( idCust , name , email , address , city) VALUES (1 , 'Per' , 'pda@eal.dk' , 'Mystreet 1' , 'Odense' ) , (2 , 'Artur' , 'at@hotmail.com' , 'Allstreet 741' , 'Vilnius' ), (3 , 'Alice' , 'ab@gmail.com' , 'Topstreet 56' , 'London' );

To select all of the enties in the created table, the following command is executed:
SELECT * FROM customerTable;

The following screenshot is the result in the command terminal:

 5.  Special dot commands to sqlite3
Most of the time, sqlite3 just reads lines of input and passes them on to the SQLite library for execution. But input lines that begin with a dot (".") are intercepted and interpreted by the sqlite3 program itself. These "dot commands" are typically used to change the output format of queries, or to execute certain prepackaged query statements. 
For a listing of the available dot commands, you can enter ".help" at any time.
Reference2
 6.  Writing results to a file
To write the result of the query to a file, in this case a .txt file the followng commands are executed:
.mode column
This command sets the mode in which the output will be organized in. 
.header on
This command sets the header of the colums on. 
.output customerTable_1.txt
This command sets the name of the file. 
SELECT * FROM tableCustomer
.exit

The screenshot showcased bellow proves the existence of the file. 

The following screenshot showcases the content of the .txt file created.

 7.  Recovery
The backup and recovery process of a SQLite database is done with the following commands.
The first command creates the backup, whilst the second one recovers it from the same file.
.backup  customerTable_recovery
.restore customerTable_recovery
 8.  How to use SQLite with Python application
Please note: I am yet to find a nice way to copy as RTF in LibreOffice (The text editor I am using at the current time) from Atom (The code editor I am using at the current time), so I will add links to the full code wherever is needed and snippets will be used for explanation. 

The way to connect Python and SQLite is to use the “sqlite3” module. The code snippet that fulfills that is: 
import sqlite3

The entire code with comments can be found here3.
 9.  UPDATE

The entire code with comments can be found here4. 

Note to lecturer:
I had a lot of misfortune with this hand-in – I had to reinstall my system, all of my test results got deleted. I am having trouble installing the needed modules that I have used in the code.
 10.  Create a GUI
Note: A full CRUD was created. 
 11.  Create a GUI to do full CRUD5
Please note: I am yet to find a nice way to copy as RTF in LibreOffice (The text editor I am using at the current time) from Atom (The code editor I am using at the current time), so I will add links to the full code wherever is needed and snippets will be used for explanation.
Note 2: For a full testing and replication, please git clone the entire repository, as it contains the initial database for this chapter.  
In a terminal enter: git clone https://github.com/lydiavasileva/sqlite-python-assigment.git

The following screenshot showcases the GUI of the program as it looks when it is started up. 
The interface has 5 entry boxes, 7 buttons and one display text widget, which at the start is empty. 









In the following screenshot is showcased what happens once the “Show” button is clicked. Note: The database selected was pre-made in the previous steps.














In the following screenshot is showcased what happens once the “Insert” button is clicked. The fields are to be filled by the user and the button “Insert” is clicked. To test if the operation is successful, the “Show” button is clicked and the new entry should be there. 













In the following screenshot is showcased what happens one the “Clear Entry” button is clicked. The entry fields are cleared out, so a new entry can be entered.














In the following screenshot is showcased what happens once the “Update” button is clicked. The fields are to be filled by the user and the button “Update” is clicked. To test if the operation is successful, the “Show” button is clicked and the updated entry should be there. Note: This cannot work if the ID entered DOES NOT EXIST in the database. 











In the following screenshot is showcased what happens once the “Delete” button is clicked. The fields are to be filled by the user and the button “Delete” is clicked. To test if the operation is successful, the “Show” button is clicked and the entry selected should be gone. Note: The user could only enter the ID for an entry to be deleted, as shown in the screenshot. 












In the following screenshot is showcased what happens once the “Help” button is clicked. A new window pops-up with a short description on each entry box.



 12.  Test section
 13.  Student Chapter
 13.1.  Creating a Web-frame
