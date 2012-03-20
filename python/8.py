#!/usr/bin/python

#get input file
inFile = open('8.txt').read().strip()

#initialize max number
maxNum = 0

#go through all numbers
for i in range(len(inFile)-4):
	currentVal = int(inFile[i]) * int(inFile[i+1]) * int(inFile[i+2]) * int(inFile[i+3]) * int(inFile[i+4])
	if currentVal > maxNum:
		maxNum = currentVal

print maxNum
