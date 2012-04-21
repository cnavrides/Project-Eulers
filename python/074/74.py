#!/usr/bin/env python
from common import memo
#returns the factoral of the number 
def sumFact(num):
	global facts
	total = 0
	for i in str(num):
		total += facts[int(i)]
	return total

#value of factorials
facts = [1]
for i in range(1,10):
	facts.append(facts[i-1] * i)

#holds the chain
nums = {}
#attach a memory function
sumFact = memo(sumFact)
#count of the number of numbers that have chain = 60
count = 0

#for all numbers less than 1,000,000
for i in range(0, 1000000):
	#add the number to the chain
	nums[i] = 0
	j = sumFact(i)
	#while the chain number isn't in the chain already
	while j not in nums:
		nums[j] = 0
		j = sumFact(j)
	#if its length is 60
	if len(nums) == 60:
		count += 1
	#reset the chain
	nums.clear()
print count	
