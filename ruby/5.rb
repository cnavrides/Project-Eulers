#!/usr/bin/ruby
#primes under 20
primes = [2,3,5,7,9,11,13,17, 19]

#largest number in the series no 11 or 20 because they are covered in changevalue
numbers = [12, 13, 14, 15, 16, 17, 18, 19]

#this is the number that is divisible by both 20 and 11
changeVal = 220

current = 220
while(true)
	isDone = true
	numbers.each do |val|
		if current % val != 0
			isDone = false
			break
		end	
	end
	if isDone == true
		puts current
		exit
	end
	current += changeVal
end

puts current
