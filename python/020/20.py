#/usr/bin/bash

#value of the result of doing a factorial 
num = 1

#size of factorial
size = 100

#find factorial
for i in range(size):
	num *= (i+1)

#convert to string
numString = str(num)

#value of the result of adding digits
finalValue = 0

#go through each digit
for number in numString:
	finalValue += int(number)

print finalValue
