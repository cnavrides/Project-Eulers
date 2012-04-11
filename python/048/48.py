#!/usr/bin/env python

total = 0

#go through all numbers
for i in range(1, 1001):
	total += (i ** i) % 10**10

print total % 10 ** 10
