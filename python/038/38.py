#!/usr/bin/env python
#from common import isPandigital
from common import *

maxNum = 0
#for all values
for a in range(1, 100000):
	#for all lengths of n
	for b in range(2, 10):
		tmp = ""
		#check if it's pandigital
		for c in range(b):
			tmp += str(a*(c+1))
		if isPandigital(tmp) and int(tmp) > maxNum:
			maxNum = int(tmp)

print maxNum



