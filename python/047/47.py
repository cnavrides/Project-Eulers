#!/usr/bin/env python
from common import getPrimes
#will return a list of the factors of the number
def getFactors(num):
	global primes
	factors = []
	i = 0
	s = num
	#go while the prime is less than the number
	while primes[i] < s and num != 1:
		#if this prime is a factor
		if num % primes[i] == 0:
			f = primes[i]
			count = 1
			num /= f
			#cover the case where it is a prime to a power
			while num % f == 0:
				count += 1
				num /= f
			factors.append(f**count)
			
		i += 1 
	return factors

#will check if the solution is correct
def check():
	global factors
	nums = []
	#for all the factors
	for i in factors:
		#if there aren't 4 factors
		if len(i) != 4:
			return False
		for j in i:
			nums.append(j)
	nums.sort()
	#make sure none of them are the same
	for i in range(len(nums)-1):
		if nums[i] == nums[i+1]:
			return False
	return True

#get primes under 100,000
maxNum = 200000
primes = getPrimes(maxNum)

factors = [[], [], [], []]

#start with the last given number
factors[0] = list(getFactors(644))
factors[1] = list(getFactors(645))
factors[2] = list(getFactors(646))
factors[3] = list(getFactors(647))

currentNum = 648
count = 4

#loop through all the numbers
while (True):
	factors[count%4] = list(getFactors(currentNum))
	#if found  break out of the loop
	if len(factors[count%4]) == 4 and check():
		break

	currentNum += 1
	count += 1

#print answer
print currentNum - 3

