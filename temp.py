#!/usr/bin/python
# Chris Heiner
# Lab 4 - Temp
# CS 3030 - Scripting Languages

#Function for Fahrenheit to Celsius calculation
def fahrenheitToCelsius(fahrenheit):
	return ((fahrenheit - 32.0) * (5.0 / 9.0))

#Function for Celsius to Fahrenheit calculation
def celsiusToFahrenheit(celsius):
	return ((9.0 / 5.0) * celsius + 32.0)

#Welcome message, continuous loop, and exception handling

#Print welcome outside of loop
print("\nWelcome to the CS 3030 Temperature Conversion Program")

#Endless loop until 3 is entered to exit program
while True:

	#Menu Print
	print("\nMain Menu\n")
	print("1:Fahrenheit to Celsius")
	print("2:Celsius to Fahrenheit")
	print("3:Exit program")
	
	#read raw user input
	x = raw_input("\nPlease enter 1, 2 or 3:")

	#If 3 is entered, exit immediately
	if x == "3":     #3 is in quotes as raw_input makes x a string type variable.  When I tried putting it in the try block below, it caused problems.
		exit(0)

	#Exception handling, verify user input is an integer.  When continue is executed, it starts the loop over on the next iteration.
	try:
		x = int(x) #casting x as an int type
		
		#If x is an integer other than 1, 2, or 3, print an error message
		if x !=1 and x != 2:
			print("Invalid entry: Your input must be 1, 2, or 3")
			continue

		#F to C conversion if x is an integer of value 1
		if x == 1:
			fDeg = raw_input("\nPlease enter degrees Fahrenheit:")
		
			#When calling F to C conversion, we need to verify the raw input is a float type, otherwise it will print an informative error
			try:
				fDeg = float(fDeg) #casting fDeg as a float
				print("\n%.1f degrees Fahrenheit equals %.1f degrees Celsius" % (fDeg, fahrenheitToCelsius(fDeg)))
			except:
				print("\nInvalid entry: Your input must be a whole number or floating point without commas (Ex: 21.3 or 2201)")
				continue

		#C to F conversion if x is an integer of value 2
		if x == 2:
			cDeg = raw_input("\nPlease enter degrees Celsius:")
			
			#When calling C to F conversion, raw input must be a float type, otherwise it will print an informative error
			try:
				cDeg = float(cDeg) #casting cDeg as a float
				print("\n%.1f degrees Celsius equals %.1f degrees Fahrenheit" % (cDeg, celsiusToFahrenheit(cDeg)))
			except:
				print("\nInvalid entry: Your input must be a whole number or floating point without commas (Ex: -21.3 or 1211)")
				continue
		
	except:
		
		print("\nInvalid entry")
		continue
