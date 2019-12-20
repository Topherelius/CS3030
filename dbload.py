#!/usr/bin/python
# Chris Heiner
# Lab 5 - Database Loader
# CS 3030 - Scripting Languages

import sqlite3
import csv
import sys


#Making sure the number of commandline arguments is correct
if len(sys.argv) != 3:
	print("Usage:./dbload INPUTCSV OUTPUTDB")
	exit(1)

#Creating the variables coming from cmd line
inputcsv = str(sys.argv[1])
db = str(sys.argv[2])

#Attempt to open the CSV file in try and utilize except if it can't be opened
try:
	open(inputcsv, 'r')

except:
	print("Error: Unable to open CSV file")
	exit(1)

#Attempt to open/connect to the database in try and utlize except if there are errors
try:
	conn = sqlite3.connect(db)
	curs = conn.cursor()

except:
	print("Error: Unable to make connection to database")
	exit(1)

#Execute statements: Create the classes table and create students table
curs.execute('''drop table if exists classes''')
curs.execute('''create table classes 
	(id text, subjcode text, coursenumber text, termcode text)''')

curs.execute('''drop table if exists students''')
curs.execute('''create table students
	(id text primary key unique, lastname text, firstname text, major text, email text, city text, state text, zip text)''')

#Every record in the CSV file is added to students table and classes table in the DB
reader = csv.reader(open(inputcsv, 'r'), delimiter=',', quotechar='"')

counter = 0

for row in reader:
	counter +=1 #Make sure to skip header
	if counter == 1:
		continue

	#Split the subject code and the course number
	sc = row[5].split(" ")
	c = (row[0], sc[0], sc[1], row[6])
        s = (row[0], row[2], row[1], row[4], row[3], row[7], row[8], row[9])

	#See if a student exists in students table and if not, insert them
	curs.execute("select * from students where id = '{0}'".format(row[0]))
	if not curs.fetchone():
		curs.execute('''insert into students(id, lastname, firstname, major, email, city, state, zip) values (?,?,?,?,?,?,?,?)''', s)
	
	#Link students with the classes table
	curs.execute('''insert into classes (id, subjcode, coursenumber, termcode) values (?,?,?,?)''', c)

#Commit once for speed
conn.commit()
conn.close()
exit(0)
