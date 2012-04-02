#!/usr/bin/python
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

#set the total to 0
total = 0
#go through all numbers (1, 10000]
for a in range(1, 10000):
	b = sum(factors(a))
	#if d(a) == d(b) and a != b add to total 
	if a != b and a == sum(factors(b)):
		total += a

#print the total
print total
