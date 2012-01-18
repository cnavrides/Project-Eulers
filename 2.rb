#the sum of the numbers, start @ 2 to inclue the 2 that won't get caught by the temp
sum = 2 
highVal = 4000000
first = 1
second = 2
temp = first + second

#loop while the next numver is less than the highValue
while temp < highVal do
	if temp % 2 == 0 
		sum += temp
	end 
	temp = first + second
	first = second
	second = temp
end   
	
#print the sum
puts sum

