#!/usr/bin/python
from decimal import * 

getcontext().prec =1000 

def getPatternLength(value):
	#sequence = str(Decimal(1) / Decimal(value)).split('.')[1]
	
	sequence = float(Decimal(1) / Decimal(value))
	print sequence

#highest number to check
#maxNumber = 1000
maxNumber = 10
#maximum value
maxVal = 0

for i in range(2, maxNumber+1):
#	print Decimal(1) / Decimal(i)
	getPatternLength(i)
 
