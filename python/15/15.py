#!/usr/bin/python

total = 0
size = 20

# go through all possibilitiesand when it hitsthe end increase by 1
def count(x, y):
	global total
	if x < size:
		count(x+1, y)
	if y < size: 
		count (x, y+1) 
	if x == y == size:
		total += 1
count(0,0)

print total
