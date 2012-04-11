#!/usr/bin/env python
from math import factorial
total = 0

#go through and check all numbers below 100,000
for i in range(3, 100000):
	factorialSum = 0
	#get the factorial of digits
	for a in str(i):
		factorialSum += factorial(int(a))

	#if the factorial sum and the number are the same add to total
	if i == factorialSum:
		total += i

print total

