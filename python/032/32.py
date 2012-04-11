#!/usr/bin/env python

numbersFound = {}

#initial min & max number
minNum = 1000
maxNum = 10000

first = True
#go through multiplicand
for a in range(1, 100):
	#if a is 10, change min & max
	if a == 10:
		minNum = 100
		maxNum = 1000 

	#go through multiplier
	for b in range(minNum, maxNum):
		#array of numbers used
		numsUsed = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		tmp = str(a) + str(b) + str(a*b)
		#if the length isn't right
		if len(tmp) != 9:
			continue
		#go through each digit
		for c in tmp:
			if numsUsed[int(c)] != 0:
				numsUsed[int(c)] = 100
				break
			else:
				numsUsed[int(c)] = 1
		#if the the product hasn't been found and all numbers used add it 
		if not numbersFound.has_key(a*b) and sum(numsUsed) == 10:
			numbersFound[a*b] = 0


print sum(numbersFound.keys())

