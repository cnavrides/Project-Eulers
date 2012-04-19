#!/usr/bin/env python
from common import isPandigital, getPrimes

#get list of primes under 10 digits
primes = getPrimes(1000000000)

length = len(primes) -1

for i in range(length):
	if isPandigital(str(primes[length - i]), len(str(primes[length - i]))):
		print primes[length - i]
		exit()


print "No luck..."
