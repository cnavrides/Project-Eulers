#!/usr/bin/env python

#brute force method
myString = ""
i = 1
#keep appending to string until it has 1,000,000 charactersn
while len(myString) < 1000000:
	myString += str(i)
	i += 1

#multiply the numbers requested
print int(myString[0]) * int(myString[9]) * int(myString[99]) * int(myString[999]) * int(myString[9999]) * int(myString[99999]) * int(myString[999999])	
