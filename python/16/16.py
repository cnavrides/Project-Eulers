#!/usr/bin/python
#get the numbers
number = str(2 ** 1000)

total = 0

#go through each digit
for digit in number:
	total += int(digit)

print total
