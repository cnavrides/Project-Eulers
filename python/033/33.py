#!/usr/bin/env python
from fractions import gcd

#hold numerators
numerator = 1
denominator = 1
count = 0

#go through every possible numerator
for a in range(12, 100):
	b1 = str(a)[0]
	b2 = str(a)[1]
	
	#for each possible reducable denominator
	for c in range(1,10):
		#eliminate the easy ones
		if a % 10 == 0:
			continue
		#get the permutations
		n1 = int(b1 + str(c))
		n2 = int(str(c) + b1)
		n3 = int(b2 + str(c))
		n4 = int(str(c) + b2)
		
		#check each value
		if a < n1:
			if float(a%10)/int(n1%10) == float(a) / n1:
				numerator *= a
				denominator *= n1
		if a < n2:
			if float(a%10)/int(str(n2)[0]) == float(a) / n2:
				numerator *= a
				denominator *= n2
		if a < n3:
			if float(int(str(a)[0]))/int(n3%10) == float(a) / n3:
				numerator *= a
				denominator *= n3
		if a < n4:
			if float(int(str(a)[0]))/int(str(n4)[0]) == float(a) / n4:
				numerator *= a
				denominator *= n4

#get the greatest common denominator
d = gcd(numerator, denominator)
	
#print the reduced fraction
print denominator/d
		
