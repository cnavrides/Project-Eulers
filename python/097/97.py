#!/usr/bin/env python
#starting number
num = 28433

# 2 to the power
for i in range(7830457):
	num = (num * 2) % (10 **10)

#add 1
print (num+1) % (10 **10)

