import math 
  
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count


t = input()

for x in xrange(0, t):

	noOfQueries = input()

	numbers = set()
	E = 0
	O = 0

	for y in xrange(0, noOfQueries):
		currentNumber = input()

		noOfSetBits = countSetBits(currentNumber)

		if not currentNumber in numbers:
			if noOfSetBits % 2 == 0:
				#the current number have even set bits
				E = E*2 + 1
				O = O*2
			else:
				#current number has odd set bits
				currentEvenCount = E
				E += O
				O += currentEvenCount + 1

			numbers.add(currentNumber)
			newNumbers = set()
			for n in numbers:
				if n != currentNumber:
					newNumber = n ^ currentNumber
					newNumbers.add(newNumber)
			numbers.update(newNumbers)

		print(str(E) + " " + str(O))

