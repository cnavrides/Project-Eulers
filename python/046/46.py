#!/usr/bin/env python
from common import getPrimes
from math import sqrt
#get primes under 100,000
maxNum = 100000
primes = getPrimes(maxNum)
primes.insert(0,1)

#index of the maxPrime
maxPrime = 0
#starting number
num = 9
while(num < maxNum):
	#up the maxPrime
	while primes[maxPrime] < num:
		maxPrime += 1
	
	#if the number is prime
	if num == primes[maxPrime]:
		num += 2
		continue

	found = False
	#go through all primes looking for a number that fits
	for i in range(maxPrime-1):
		if str(sqrt((num - primes[i])/2)).split('.')[1] == '0':
			found = True
			break

	#if no number found
	if not found:
		print num 
		break
	num += 2
