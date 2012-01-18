#the sum of the numbers
sum = 0

highVal =1000
#start at 3 and go to below the high value
for i in 3..(highVal - 1)  do
	#if it divisible by 3 or 5, add the value to the sum
	if i%3 == 0 or i%5 ==0
		sum += i
	end 
end

#print the sum
puts sum

