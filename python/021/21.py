#!/usr/bin/python
from common import factors
#set the total to 0
total = 0
#go through all numbers (1, 10000]
for a in range(1, 10000):
	b = sum(factors(a))
	#if d(a) == d(b) and a != b add to total 
	if a != b and a == sum(factors(b)):
		total += a

#print the total
print total
