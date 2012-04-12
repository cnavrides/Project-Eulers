#!/usr/bin/env python
#checks if the string passed in is pandigital (1-9)
def isPandigital(num):
	usedNumbers = [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for n in num:
		if usedNumbers[int(n)] == 0:
			usedNumbers[int(n)] = 1
		else:
			return False
	return True

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



