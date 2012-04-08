#!/usr/bin/python

#find all the divisors in x
def divisors(x):
	count = 1
	for i in range(2, x/2):
		if x % i == 0:
			count += 1
#start at 1
num = 1
total = 1

#lop until the number of divisors for the total is greater than 500
while (divisors(total) > 500): 
	num += 1
	total += num

#print the answer
print total
