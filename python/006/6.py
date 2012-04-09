#!/usr/bin/python

#what range to go through
rangeVal = 100

#initialize variables
sumSquare = 0
squareSum = 0

#loop through values
for i in range(rangeVal):
	sumSquare += (i+1)**2
	squareSum += i+1
#square the sum
squareSum *= squareSum

#return result
print squareSum - sumSquare
