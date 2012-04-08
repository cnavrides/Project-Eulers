#!/usr/bin/python
#import the factors common function
from common import factors

def isAbundant(value):
	#get the global list of abundant numbers
	global abundantNumbers
	
	#for each abundant number
	for i in abundantNumbers:
		try:
			#if the abundant number is more than half of the number I am looking at exit as
			#it can't be written as an abundant number
			if i > value/2:
				return False
			tmp = abundantNumbers.index(value-i)
			return True
		except:
			continue
	return False

#largest number that can't be written as sum of 2 abundeant numbers
maxNumber = 28123

#list of abundunt numbers
abundantNumbers = []

#sum of numbers that cant be added up by 2 abundant numbers
total = 0

#go through all numbers below max
for i in range(1, maxNumber+1):
	#get the sum of the factors and append to abundant if it is
	if sum(factors(i)) > i:
		abundantNumbers.append(i)
	
	#if it is now abundant add to total
	if not isAbundant(i):
		total += i
	
print total
			

