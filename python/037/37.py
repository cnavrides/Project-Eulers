#!/usr/bin/env python
#list of primes
primes = [2,3, 5, 7]
#current number
number = 11

#how many primes found
count = 0
#total of those primes found
total = 0

#find the primes using the sieve of erodes
while True:
	isPrime = True
	#check the number against known primes
	for p in primes:
		if number % p == 0:
			isPrime = False
			break
	#if it is a prime append and check truncatable
	if isPrime == True:
		primes.append(number)
		truncatable = True
		#see if it is truncatable
		for i in range(1, len(str(number))):
			#left to rigt
			if not int(str(number)[i:]) in primes:
				truncatable = False
				break
			#right to left
			if not int(str(number)[:len(str(number))-i]) in primes:
				truncatable = False
				break
		#if it's truncatable
		if truncatable:
			count += 1
			total += number
			#if it's the 11th one
			if count == 11:
				break
	number += 2 

print total
