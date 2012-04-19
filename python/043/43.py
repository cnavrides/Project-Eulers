#!/usr/bin/env python
#returns the number if it is substring divisible, 0 otherwise
#takes a string as the number
def subStringDivisible(num):
	primes = [2, 3, 5, 7, 11, 13, 17]
	#go through each prime
	for i in range(len(primes)):
		#if the number isn't divisible by the prime return false
		if int(num[i+1] + num[i+2] + num[i+3]) % primes[i] != 0:
			return 0 
	return int(num)


#recursive function that will search all permutations
#num is a list of the current number so far
#perm is a list of the numbers available for permutations
def permutation(num, perm):
	#how many numbers to do permutations for
	s = len(perm)
	count = 0
	#if there aren't any numbers
	if s == 0:
		#check if the number is prime
		numToCheck = ''.join(num)
		#if it is prime, print it
		return subStringDivisible(numToCheck)
	
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
			count += permutation(tNum, tPerm)
	return count

#all the numbers
numbers = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

#print the output
print permutation([], numbers)
