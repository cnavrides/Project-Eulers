#!/usr/bin/python
#days in each month
daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#starting day(January 1st) in 1901 was a tuesday
day = 1

#number of times that a sunday falls on first day of the month 
sundayCount = 0

#for each month in 100 years
for i in range(1, 101):
	#for each month in the year
	for j in range(12):
		#if it starts on a sunday
		if day == 6:
			sundayCount += 1
		#if it's a leap yearand february
		if i % 4 == 0 and j == 1:
			day = (day + daysPerMonth[j] + 1) % 7
		else:
			day = (day + daysPerMonth[j]) % 7

#print the count
print sundayCount

