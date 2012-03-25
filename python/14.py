#!/usr/bin/python
from common import *

#get the chain Recursive
def chain(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		return 1 + chain(x/2)
	else:
		return 1 + chain(3*x+1)

chain = memo(chain)

maxChain = 0
maxNumber = 0
#go through all numbers under 1000000
for i in range(2, 1000000):
	tmp = chain(i)
	if tmp > maxChain:
		maxChain = tmp
		maxNumber = i

print maxNumber
