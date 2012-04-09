#!/usr/bin/python
def letterCount(maxNumber):
	#number of letters forvalues under 20
	numLetters = ["", "one","two","three","four","five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

	#number of letters for values to one hundred
	numTensPlace = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	#characters for 'hundred'
	hundredLetters =7

	#letters in 'thousans'
	thousandLetters = 8

	#the letters for and
	andLetters = 3

	letters = 0
	for i in range(1,maxNumber+1):
	#	print i
		
		#thousand
		if i >= 1000:
			letters += thousandLetters
			letters += len(numLetters[int(str(i)[0])])
			
		#Hundred
		y = i % 1000
		if y >= 100:
			letters += len(numLetters[int(str(y)[0])])
			letters += hundredLetters
		
		#Tens and ones
		x = i % 100
		if x != 0 and i > 100:
			letters += andLetters
		if x >= 20:
			letters += len(numTensPlace[int(str(x)[0])])
			letters += len(numLetters[int(str(x)[1])])
		else:
			letters += len(numLetters[x])

	return letters

#how high to go to
maxVal = 1000

print letterCount(maxVal)

