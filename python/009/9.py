#!/usr/bin/python
import math

#iterate up through half of sum total
for a in range(2, 500):
	#since b has to be larger that a
	for b in range(a+1, 500):
		c = a ** 2 + b ** 2
		if a + b + math.sqrt(c) == 1000:
			print a * b * math.sqrt(c)
			exit()
