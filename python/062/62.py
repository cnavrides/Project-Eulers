#!/usr/bin/env python
#returns a list that is the string of the num count
#this is used as a hash to count the # of permutations
def getPermutations(number):
	counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	num = str(number)
	for d in num:
		counts[int(d)] += 1

	return str(counts)
	
#counts number of permutations
permCounts = {}

#lowest number for that cube
lowestPerm = {}

#go through all numbers under 1 million
for i in range(346, 1000000):
	#get the hash of that cube
	val = getPermutations(i**3)

	#if it exists add 1 to that count, otherwise add that hash
	if permCounts.has_key(val):
		permCounts[val] += 1
	else:
		permCounts[val] = 1
		lowestPerm[val] = i**3

lowest = -1
#go through the hash keys
for x in permCounts:
	#if there were 5 permutations 
	if permCounts[x] == 5:
		#if this one is first or the lowest
		if lowest < 0 or lowestPerm[x] < lowest:
			lowest = lowestPerm[x]

print lowest 
