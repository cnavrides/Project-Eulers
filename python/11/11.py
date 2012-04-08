#!/usr/bin/python

inFile = open('11.txt')

#hold the numbers 
numbers = []

#go through each line and add the numbers to the array
for line in inFile:
	numbers.append(line.strip().split(' '))

#max product
maxNum = 0

#go through horizontally
for row in numbers:
	for i in range(len(row)-3):
		product = int(row[i]) * int(row[i+1]) * int(row[i+2]) * int(row[i+3])
		if product > maxNum:
			maxNum = product 

#go through vertically
for x in range(len(numbers)-3):
	for y in range(len(numbers[x])):
		product = int(numbers[x][y]) * int(numbers[x+1][y]) * int(numbers[x+2][y]) * int(numbers[x+3][y])
		if product > maxNum:
			maxNum = product 

#go through right to left diagonal  
for x in range(len(numbers)-3):
	for y in range(len(numbers[x])-3):
		product = int(numbers[x][y]) * int(numbers[x+1][y+1]) * int(numbers[x+2][y+2]) * int(numbers[x+3][y+3])
		if product > maxNum:
			maxNum = product 

#go through left to right diagonal  
for x in range(len(numbers) - 3):
	for y in range(len(numbers[x]) - 3):
		a = len(numbers[x]) - y-1 
		product = int(numbers[x][a]) * int(numbers[x+1][a-1]) * int(numbers[x+2][a-2]) * int(numbers[x+3][a-3])
		if product > maxNum:
			maxNum = product 


print maxNum
