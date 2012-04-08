#!/usr/bin/python
#get the memo function from common
from common import memo

def fib(n):
	if n == 2 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#attach memory function to fibinoci function
fib = memo(fib)

#how many digits to look for
numDigits = 1000

#largest number given in problem
count = 12

#loop while the number of digits is less than 1000
while(len(str(fib(count))) < 1000):
	count += 1

#print result
print count
