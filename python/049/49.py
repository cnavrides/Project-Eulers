#!/usr/bin/env python
from common import getPrimes
#returns the sorted list of the digits
def digits (num):
	x = []
	for l in str(num):
		x.append(l)
	return sorted(x)

#get all primes under 10,000
primes = getPrimes(10000)

#put the primes in a has table
hashPrimes = {}
for p in primes:
	hashPrimes[p] = 0

#go through all primes
for i in range(len(primes)):
	#don't bother if under 1000
	if primes[i] < 1000:
		continue
	#go through remaining primes
	for j in range(i+1, len(primes)):
		difference = primes[j] - primes[i]
		n3 = primes[j] + difference
		#if n3 is a prime and all primes have the same digits and it isn't the given solution
		if hashPrimes.has_key(n3) and (digits(primes[i]) == digits(primes[j]) == digits(n3)) == True and primes[i] != 1487:
			print primes[i], primes[j], n3
			exit()
