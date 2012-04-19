#!/usr/bin/env python
#list of numbers
numbers = {}
#get all the pentagonal numbers and store in hash table
for i in range(1, 10000):
	numbers[i*(3*i-1)/2] = 0
#list of the numbers
nums = sorted(numbers.keys())
#list of the d-values
dValues = []

found = False
#go through all combinations
for i in range(len(nums)-1):
	for j in range(i+1, len(nums)):
		#check if the number is pentagonal
		if numbers.has_key(nums[j] + nums[i]) and numbers.has_key(nums[j] - nums[i]):
			dValues.append(nums[j] - nums[i])

#print the lowest number that is pentagonal
print sorted(dValues)[0]



