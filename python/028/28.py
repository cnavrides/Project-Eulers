#!/usr/bin/python

#size of spiral	
size = 1001 

#total value of edges
total = 1 

#allocate array to all -1's
myArray = [[-1 for col in range(size)] for row in range(size)]

#how many to go over by
length= 2

#set starting values
x = size/2
y = size/2

#set middle as 0
myArray[x][y] = 1

#initialize the counting variable
count = 2

#move one to the right for starting value
x+= 1

#keep in the loop until all values have been counted
while count < size**2:
	#down
	for i in range(length):
		myArray[x][y] = count
		y += 1
		count += 1	
	
	#at the edge, add the total
	total += count -1

	#went to many, and reset	
	y -= 1	
	x -= 1
	#left
	for i in range(length):
		myArray[x][y] = count
		x -= 1
		count += 1	

	#at the edge, add the total
	total += count -1

	#went to many, and reset	
	x += 1
	y -= 1
	#up
	for i in range(length):
		myArray[x][y] = count
		y -= 1
		count += 1	

	#at the edge, add the total
	total += count -1
	
	#went to many, and reset	
	y += 1
	x += 1
	#right
	for i in range(length):
		myArray[x][y] = count
		x += 1
		count += 1	
	
	#at the edge, add the total
	total += count -1

	#increment length
	length+= 2	

#print the total
print total
