#!/usr/bin/python
from functools import wraps
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

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap


count = memo(count)
x = count(0,0)
print x

