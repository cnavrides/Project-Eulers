#!/usr/bin/env python
#returns True if the number returned is bouncy
def isBouncy(n):
	#if it is less than 3 digits return false
	if n < 100:
		return False
	
	#convert the number to a string
	num = str(n)

	#going up and down
	up = False
	down = False	

	#get the previous number for comparision
	previous = int(num[0])
	#for the 2nd digit through 
	for d in num[1:]:
		if previous > int(d):
			down = True
		elif previous < int(d):
			up = True
		#if it has gone both up & down return True
		if down and up:
			return True
		#set previous to the current
		previous = int(d)
	return False

bouncy = 0 
current = 1 
#go through while the percentage isn't 99%
while( (1.0 * bouncy/current) != .99):
	current += 1
	if isBouncy(current):
		bouncy += 1

print current
