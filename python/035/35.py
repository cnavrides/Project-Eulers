#!/usr/bin/env python

from common import getPrimes

#get primesbelow 1,000,000
primes = getPrimes(1000000)

#number of circular primes
count = 0

#go through all the primes
for i in primes:
	circular = True
	numDigits = len(str(i))
	#go through the circle
	for a in range(1, numDigits):
		tmp = ""
		#build the new number
		for b in range(numDigits):
			tmp += str(i)[(a+b)%numDigits]

		#if the number isn't a prime, exit
		if not int(tmp) in primes:
			circular = False
			break
	if circular:
		count += 1

print count
