#!/usr/bin/python

#get input file
inFile = open('13.txt')

#set total to 0
total = 0

#go through each line and add to total
for line in inFile:
	total = total + int(line.strip()) 

#convert to string then print the first 10 characters
print str(total)[0:10]

