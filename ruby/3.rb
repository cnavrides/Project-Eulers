#
# Not the most efficient way but first find all primes from 2 to Sqrt(number)
# Then reverse the list of primes, then go through and find the first prime
# that can divide the number. 
#
# Doing it this way to re-use the prime finding code if I need to
#
number = 600851475143
sqrtNumber = Math.sqrt(number)
value = 3
highestValue = 3
primes = [2]

#get a list of all primes under sqrt(number)
while value <= sqrtNumber do
	isPrime = true
	primes.each do |p|
	  if value % p == 0
	    isPrime = false
	    break
	  end
  end
  if isPrime == true
    primes << value
  end
  value += 2
end

primes = primes.reverse

primes.each do |p|
  if number % p == 0
    puts p
    break
  end
end
