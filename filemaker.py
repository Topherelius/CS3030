#!/usr/bin/python
# Chris Heiner
# Lab 6 - Filemaker
# CS 3030 - Scripting Languages

import sys
import random
import shlex

#Check for correct number of cmd line arguments
if len(sys.argv) != 4:
	print("Usage: ./filemaker INPUTCOMMANDFILE OUTPUTFILE RECORDCOUNT")
	exit(1)

#Create variables to store arguments
incmdfile = sys.argv[1]
outfile = sys.argv[2]
recordcnt = sys.argv[3]

#Check count and ability to open files
try:
	recordcnt = int(recordcnt)
except:
	print("Error, count is NAN or is negative")
	exit(1)

try:
	inputFile = open(incmdfile, "r")
except:
	print("Error, unable to open input file")
	exit(1)
    
try:
	outputFile = open(outfile, "w")
except:
	print("Error, unable to open output file")
	exit(1)

#Create command list and randomFiles dictionary
commands = []
randomFiles = {}

for line in inputFile.readlines():
	cmd = shlex.split(line,True)

	if cmd[0] == "HEADER":
		outputFile.write(cmd[1].decode('string_escape'))
		continue
	elif cmd[0] == "FILEWORD":
		inFile = open(cmd[2], "r")
		randomFiles[cmd[2]] = inFile.readlines()
		inFile.close()
	commands.append(cmd)

#Loop through record count amount
for i in range(recordcnt):
	randomData = {}
	
	#Generate data for randomData
	for cmd in commands:
		if cmd[0] == "STRING" or cmd[0] == "REFER":
			continue
			
		elif cmd[0] == "FILEWORD":
			label = cmd[1]
			if label in randomData:
				print("Error, key exists")
				exit(1)
			else:
				randNum = random.randint(0, len(randomFiles[cmd[2]])-1)
				randWord = (randomFiles[cmd[2]][randNum]).rstrip()
				randomData[cmd[1]] = str(randWord)
				
		elif cmd[0] == "NUMBER":
			label = cmd[1]
			minNum = int(cmd[2])
			maxNum = int(cmd[3])
			if label in randomData:
				print("Error, key exists")
				exit(1)
			else:
				randNum = random.randint(minNum, maxNum)
				randomData[cmd[1]] = str(randNum)
				
	#Generate some output baby!
	for cmd in commands:
		if cmd[0] == "STRING":
			outputFile.write((cmd[1]).decode('string_escape'))
		elif cmd[0] == "NUMBER":
			outputFile.write(str(randomData[cmd[1]]))
		elif cmd[0] == "FILEWORD":
			outputFile.write(randomData[cmd[1]])
		elif cmd[0] == "REFER":
			outputFile.write(str(randomData[cmd[1]]))
outputFile.close()
exit(0)
