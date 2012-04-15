#!/usr/bin/python
from functools import wraps
from math import sqrt
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
	primes = []
	nums = [True for i in range(maxVal)]
	nums[0] = False
	nums[1] = False
	sqrtVal = int(sqrt(maxVal)) + 1
	#Initialize list of values
	for i in range(2, sqrtVal):
		if nums[i]:
			j = i + i
			while j < maxVal:
				nums[j] = False
				j += i
	#find the primes using the sieve of erodes
	for i in range(maxVal):
		if nums[i]:
			primes.append(i)
	return primes

#get the factors of a number
def factors(num):
	#start list with 1
	factors = [1]
	
	#offset to add one to odd numbers
	offset = 1
	if num %2 == 0 and num != 4:
		offset = 0

	#go through the first half of the list and add numbers
	for i in range(2, num/2 + offset):
		 if num % i == 0 and factors.count(i) == 0:
			factors.append(i)
			if i != num/i:
				factors.append(num/i)
	#return the list of factors
	return factors

#Tree node to use when dealing with trees
class treeNode:
	# each node can start with a value and a parent (optional)
	def __init__(self, value, parent = None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent
	#add a left node
	def addLeftNode(self, left):
		self.left = left
	#add a right node
	def addRightNode(self, right):
		self.right = right
	#add a parent node if it wasnt added in the constructor
	def addParentNode(self, parent):
		self.parent = parent

#checks if the string passed in is pandigital (1-length)
def isPandigital(num, length = 9):
	usedNumbers = [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for n in num:
		if usedNumbers[int(n)] == 0:
			usedNumbers[int(n)] = 1
		else:
			return False
	for i in range(1, length+1):
		if usedNumbers[i] != 1:
			return False
	return True
