#!/usr/bin/env python

from common import memo
#denominations of currency
values = [200, 100, 50, 20, 10, 5, 2, 1]

#recursive function to find permutations of the currency passed in
def permutations(denomination, maxNum = 200):
	count = 0
	for v in values:
		#if the number is greater than the value or max number to go to.
		if v > denomination or v > maxNum:
			continue
		#if they are equal then add 1 otherwise continue down permutations
		if v == denomination:
			count += 1
		else:
			count += permutations(denomination - v, v) 
	return count

#attach memory function to recursive function
permutations = memo(permutations)

print permutations(200)

