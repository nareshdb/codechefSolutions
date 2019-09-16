import math 
  
def sumOfDigits(num):
	n = num
	tot=0
	while(n>0):
		dig=n%10
		tot=tot+dig
		n=n//10
	return tot

t = input()

for x in xrange(1, 100):
	
	n = input()

	base = 10*n

	sumOfDigitsInBase = sumOfDigits(base)

	if sumOfDigitsInBase%10 == 0:
		print(base)
	else:
		print(base + ( int(math.ceil(float(sumOfDigitsInBase)/10.0)*10) - sumOfDigitsInBase))
