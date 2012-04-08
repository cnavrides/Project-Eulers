#!/usr/bin/python
from common import *
# Dynamic Programming implementation for Project Euler 15
size = 20 

def count(x, y):
	if x < size and y < size:
		return count(x+1, y) + count(x, y + 1)
	elif y < size: 
		return count (x, y+1) 
	elif x < size:
		return count (x+1, y)
	else:
		return 1

count = memo(count)
x = count(0,0)
print x

