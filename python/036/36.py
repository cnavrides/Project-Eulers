#!/usr/bin/env python
#returns true it the string passed in is a palindrome
def isPalindrome(num):
	size = len(num)
	for i in range(size/2):
		if num[i] != num[size - i - 1]:
			return False
	return True

total = 0
#for all numbers <= 1,000,000
for i in range(1000001):
	#if the binary and the number are palindromes add to total
	if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
		total += i
print total	
