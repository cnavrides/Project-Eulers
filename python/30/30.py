#!/usr/bin/env python

#the total of numbers found
count = 0

#go through all numbers <= 6-digits
for i in range(10, 1000000):
	tmp = 0
	#add up digits to the 5th power
	for j in str(i):
		tmp += int(j) ** 5
	#if sum is equal to the number
	if tmp == i:
		count += i

print count
