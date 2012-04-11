#!/usr/bin/env python

from common import getPrimes
from time import time
#get all primes below 1,000,000
primes = getPrimes(1000000)


maxCount = 0
maxPrime = -1

start = time()

#prime to look at
for p in primes:
	#index variable	
	i = 0
	
	#count of how many primes used
	count = 0	

	#sum of the primes so far
	total = 0

	#Start index value
	start = 0
	tooHigh = p/2

	#keep in loop until the prime is half of the one being looked at
	while primes[i] <=  tooHigh:
		#add currentPrime to total & increment count
		total += primes[i]
		count += 1
		
		#if found break		
		if total == p:
			break
		#if it's too high, take off the begining ones 
		if total > p: 
			#loop until either we have taken too many off or the total is 
			#below the prime
			while count > maxCount and total > p:
				total -= primes[start]
				start += 1
				count -= 1
			#if it is now equal break
			if total == p:
				break

		#increment index
		i += 1
	#if a combination wasfound and the number of primes was greater than current max	
	if total == p and count > maxCount:
		maxCount = count
		maxPrime = p

print maxPrime	
print time() - start	
