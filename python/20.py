#/usr/bin/bash

num = 1
for i in range(100):
	num *= (i+1)

numString = str(num)

finalValue = 0
for number in numString:
	finalValue += int(number)

print finalValue
