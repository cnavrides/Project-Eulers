import time


t0= time.clock()

val =  30

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

#copy all primes 
availablePrimes = list(allPrimes)
#copy the list of all primes
usedPrimes = {}
for p in allPrimes:
    usedPrimes[p] = []

myNumers=list(allNumbers)

#Reverse all numbers
allNumbers.reverse()

#a list of combinations
highestCombo={}


prime1 = -1
prime2 = -1
for x in allNumbers:
    val = 0

    for y in allPrimes:
        if y > x:
            break
        if x%y == 0:
            val += 1
            if val == 1:
                prime1 = y
            elif val == 2:
                prime2 = y
        if val > 2:
            break
    if val > 0 and val < 3:
        if val == 1 and prime1 in availablePrimes:
            temp =  str(prime1)+ "-" + str(prime1)
            availablePrimes.remove(prime1)
        elif val == 2 and prime1 in availablePrimes and prime2 in availablePrimes:
            temp = str(prime1)+ "-" + str(prime2)
        else:
            myNumers.remove(x)
            continue
        
        if temp in highestCombo:
            myNumers.remove(x)
        else:
            highestCombo[temp] = x
            usedPrimes[prime1].append(x)
            if val == 2:
                usedPrimes[prime2].append(x)
    else:
        myNumers.remove(x)

reverse = {}

for x in highestCombo:
    reverse[highestCombo[x]] = x


finalNumbers = []
finalPrimes = []
for num in usedPrimes:
    if len(usedPrimes[num]) == 1:
        finalNumbers.append(usedPrimes[num][0])
        finalPrimes.append(num)

for x in finalPrimes:
    del usedPrimes[x]
    del reverse[highestCombo[str(x)+'-'+str(x)]]
    del highestCombo[str(x)+'-'+str(x)]

   
#print "highestCombo: " + str(highestCombo)
#print "reverse: " + str(reverse)
#print "allPrimes: " + str(allPrimes)
#print "usedPrimes: " + str(usedPrimes)
#print "myNumbers: " + str(myNumers)


answer = sum(finalNumbers) + 1
print "answer: " + str(answer)
print "finalNumvers: " + str(finalNumbers)



print
print "len(highestCombo): " + str(len(highestCombo))
#print "len(allPrimes): " + str(len(allPrimes))
#print "len(myNumers): " + str(len(myNumers))
print

print "time taken: " + str(time.clock() - t0) + " seconds"
