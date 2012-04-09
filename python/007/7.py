#!/usr/bin/python

#naive 1:05 am implementation, will improve in the morning

#list of primes
primes = [2]

#number of primes found so far
numPrimes = 1

#current number checking
currentNum = 3

#how many primes to find before stopping
nthPrime = 10001

#loop while true
while (True):
	isPrime = True
	#check if prime
	for p in primes:
		if currentNum % p == 0:
			isPrime = False
			break
	#if it is prime, add to list
	if isPrime:
		primes.append(currentNum)
		numPrimes += 1 
		if numPrimes == nthPrime:
			break
	currentNum += 1
print currentNum 

