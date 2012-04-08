#!/usr/bin/env python

from common import *

#start by getting the list of primes to compare things to
#the 300,000 is just a guess at the upper bound of prime size
primeList = getPrimes(300000)

#since n starts at 0, b must be a prime under 1000
possibleB = getPrimes(999)

#the longest number of consecutive primes
maxCount = 0
#the product of a & b
product = 0

#go through all the possible a's
for a in range(-999, 1000):
	#go through promes below 1,000 for b
	for b in possibleB:
		count = 1
		num = b
		#go through all primes and count how many are found
		while num in primeList:
			num = count ** 2 + (a * count) + b
			count += 1
		#if the number of sequential primes is higher than current max 
		#store the value
		if count > maxCount:
			product = a * b
			maxCount = count

#print the product that produces the maximum count
print product
		
