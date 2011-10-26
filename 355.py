#!/usr/bin/python
val = 10

allPrimes = []
allNumbers = []

for x in range(val):
    num = x+1
    allNumbers.append(num)
    allPrimes.append(num)

allPrimes.remove(1)

for x in allPrimes:
    for y in allPrimes:
        if y % x == 0 and y/x != 1:
            allPrimes.remove(y)

#copy the list of all primes
usedPrimes=list(allPrimes)
myNumers=list(allNumbers)

allNumbers.reverse()

prime1 = -1
prime2 = -1
for x in allNumbers:
    val = 0
    for y in allPrimes:
        if x%y == 0:
            val += 1
            if val == 1:
                prime1 = y
            elif val == 2:
                prime2 = y
        if val > 2:
            break
    if val != 3:
        if val == 1:
            if prime1 in usedPrimes:
                usedPrimes.remove(prime1)
            else:
                myNumers.remove(x)
       # else:
       #     if prime1 in usedPrimes and prime2 in usedPrimes:
       #         usedPrimes.remove(prime1)
       #         usedPrimes.remove(prime2)
       #     else:
       #         myNumers.remove(x)
    else:
        myNumers.remove(x)

print "allPrimes: " + str(allPrimes)
print "usedPrimes: " + str(usedPrimes)
print "myNumbers: " + str(myNumers)
answer = sum(myNumers) + 1
print answer
