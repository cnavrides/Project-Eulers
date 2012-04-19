#!/usr/bin/env python
from common import isPandigital, getPrimes
from math import sqrt

#check if the number passed in is prime
def isPrime(num):	
	#if even, don't bother
	if num % 2 == 0:
		return False
	#get the squareroot
	s = sqrt(num)
	#starting value
	i = 3
	#go through (3, square root of number)
	while i < s:
		if num % i == 0:
			return False
		i += 2
	#if no number found, return true
	return True

#recursive function that will search all permutations
def permutation(num, perm):
	#how many numbers to do permutations for
	s = len(perm)
	#if there aren't any numbers
	if s == 0:
		#check if the number is prime
		numToCheck = ''.join(num)
		#if it is prime, print it
		if isPrime(int(numToCheck)):
			print numToCheck
			exit()
	else:
		#for each remaining digit
		for i in range(s):
			#get the value of the next digit
			val = perm[i]
			
			#move the digit onto the working number
			tNum = list(num)
			tNum.append(val)
			tPerm = list(perm)
			tPerm.remove(val)
			
			#check it down
			permutation(tNum, tPerm)	
			
#start with the highest possible number
startNum = "987654321"

#if none found, reduce number of digits by 1
for i in range(len(startNum)):
	permutation("",list(startNum[i:]))

#if no number found, let the user know
print "No luck..."
