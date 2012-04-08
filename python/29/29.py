#!/usr/bin/env python

#hold all numbers found
numbers ={}

#go through all permutations
for a in range(2, 101):
	for b in range(2, 101):
		num = a ** b
		#if the number hasn't been found before add it
		if not numbers.has_key(num):
			numbers[num] = 0

print len(numbers)

