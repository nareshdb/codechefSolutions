import math 
import sys
  
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 

	factors = set()

	while n % 2 == 0:
		factors.add(2),
		n = n / 2

	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3, int(math.sqrt(n))+1, 2):
		# while i divides n , print i ad divide n 
		while n % i == 0: 
			factors.add(i),
			n = n / i

	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		factors.add(n)

	return factors

t = input()

for x in xrange(0, t):

	ans = "No"

	x = 31623

	possiblePrimes = set()

	while ans == "No" or ans == -1:
		
		print("1 " + str(int(x)))
		sys.stdout.flush()

		modOfNumber = input()

		commonMultipleOfAllThePrimes = x**2 - modOfNumber

		primes = primeFactors(commonMultipleOfAllThePrimes)

		primes = [prime for prime in primes if prime >= modOfNumber]

		intersection = set(primes).intersection(possiblePrimes)
		if len(intersection) > 0:
			possiblePrimes = intersection
		else:
			possiblePrimes = primes

		if len(possiblePrimes) == 1:
			print("2 " + str(int(list(possiblePrimes)[0])))
			sys.stdout.flush()
			ans = raw_input()
		else:
			x = math.ceil(math.sqrt(max(possiblePrimes)))

