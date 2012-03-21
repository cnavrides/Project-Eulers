#class for primes 
class primes:
	#initialize with first two primes
	def __init__(self):
		self.primes = [2,3]	
	#fill prime list with value that are less than maxVal
	def getPrimes(self, maxVal):
		nums = []
		#Initialize list of values
		for i in range(maxVal+1):
			if i % 2 == 0 or i % 3 == 0 or i  < 3:
				nums.append(-1)
			else:
				nums.append(0)
		count = 0	
		#find the primes using the sieve of erodes
		for j in nums:
			if j != -1:
				isPrime = True
				for p in self.primes:
					if count % p == 0:
						isPrime = False
						break
				if isPrime == True:
					self.primes.append(count)
					tmp = count
					while tmp < maxVal:
						nums[tmp] = -1
						tmp += count
			count += 1
		return self.primes


