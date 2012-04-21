#!/usr/bin/env python
# count of how many numbers found
count = 0
#for every number. Skip 0
for i in range(1,100):
	#for every power, skip 0 as x ** 0 == 1
	for j in range(1,100):
		if len(str(i ** j)) == j:
			count += 1

print count

