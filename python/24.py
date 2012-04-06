#!/usr/bin/python
#This will hold all sorted permutations
allLists = []

#recursive function that adds to the lsit
def permutations(currentList, remainingList):
	#if there is more than 2 options
	if len(remainingList) > 2:
		#for each item, append it to the known list and then add the rest of the permutations
		for i in sorted(remainingList):
			tmp = list(currentList)
			tmp.append(i)
			tmp2 = sorted(list(remainingList))
			tmp2.remove(i)
			permutations(tmp, tmp2)
	else:
		#sort remaining 2
		sortedRemaining = sorted(remainingList)
		#add the lower one to the final list
		tmp = list(currentList)
		tmp.append(sortedRemaining[0])
		tmp.append(sortedRemaining[1])
		allLists.append(tmp)
		#add the higher one to the final lsit
		tmp = currentList
		tmp.append(sortedRemaining[1])
		tmp.append(sortedRemaining[0])
		allLists.append(tmp)

#original numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#start with empty list and all numbers
permutations([], numbers)

#print the millionth item
print allLists[999999]
