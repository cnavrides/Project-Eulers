#!/usr/bin/env python
#will r
def isTriangleWord(word):
	global triangleValues
	total = 0
	for char in word:
		total += ord(char) - 96
	if triangleValues.has_key(total):
		return 1 
	else:
		return 0

#hash of triangle numbers
triangleValues = {}
#upper bound for english words
for i in range(1,200):
	triangleValues[(i*(i+1))/2] = 0

#open file
inFile = open('words.txt')
words = inFile.read().split(',')
count = 0
#go through each value
for w in words:
	count += isTriangleWord(w.strip().lower()[1:len(w)-1])
	
print count
