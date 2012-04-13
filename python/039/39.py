#!/usr/bin/env python
import math

maxCount = 0
#go through all values of p
for p in range (12, 1001):
	count = 0
	#go through every a
	for a in range(1, p/3):
		#and all b's
		for b in range(a, 2 * p / 3):
			val = math.sqrt(a**2 + b**2)
			#if val is a whole number and a + b + val is equal to perimete add to count
			if str(val).split('.')[1] == '0'and a + b + val == p :
				count += 1
	#if this is the largest
	if count > maxCount:
		maxCount = count
		maxP = p

#print max
print maxP
