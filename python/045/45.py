#!/usr/bin/env python
#returns the triangle number for the value passed in
def triangleNum(n):
	return n*(n+1)/2
#returns the pentogonal number of n
def pentogonal(n):
	return n*(3*n-1)/2

#returns True if val is hexogonal
def hexogonal(n):
	return n*(2*n-1)

#values of first numbers
a = 286
b = 165
c = 143

#loop until number is found
while (True):
	#get the triangle number
	t = triangleNum(a)

	#up the pentogonal & hexogonal number while it is 
	#less than the triangle number
	while(pentogonal(b) < t):
		b += 1
	while(hexogonal(c) < t):
		c += 1

	#if all the numbers are equal print it out and exit
	if t == pentogonal(b) == hexogonal(c):
		print t
		break

	#up the n value of the triangle number
	a += 1
