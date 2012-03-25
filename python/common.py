#!/usr/bin/python
from functools import wraps
#memory function that stores values in recursive function 
def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap

#gets the array of prime numbers  below the value
def getPrimes(maxVal):
	primes = [2,3]
	nums = []
	#Initialize list of values
	for i in range((maxVal+1)):
		if i % 2 == 0 or i % 3 == 0 or i  < 3:
			nums.append(-1)
		else:
			nums.append(0)
	count = 0	
	#find the primes using the sieve of erodes
	for j in nums:
		if j != -1:
			isPrime = True
			for p in primes:
				if count % p == 0:
					isPrime = False
					break
			if isPrime == True:
				primes.append(count)
				tmp = count
				while tmp < maxVal:
					nums[tmp] = -1
					tmp += count
		count += 1
	return primes

