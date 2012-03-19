#!/usr/bin/python

total = 0
size = 20
# This should be using DP instead of recursion
def go():
	count (0,0)

def count(x, y):
	global total
#	print "(" + str(x) + "," + str(y) + ")" + " = " + str(total)
	if x < size:
		count(x+1, y)
	if y < size: 
		count (x, y+1) 
	if x == y == size:
		total += 1
'''
matrix = [ [ 0 for i in range(size) ] for j in range(size) ]
for i in range(size):
	matrix[i] = []
'''

go()
print total
