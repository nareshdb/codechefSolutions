import math 
  
t = input()

for x in xrange(0, t):

	noOfPeople = input()

	noOfChocolates = input()

	if noOfChocolates > noOfPeople:
		baseNumber = noOfChocolates/noOfPeople
		remainingChocolates = noOfChocolates%noOfPeople
		noOfPoepleWithBaseNoOfChocolates = noOfPeople - remainingChocolates

		if noOfPoepleWithBaseNoOfChocolates == remainingChocolates:
			print(remainingChocolates*2 - 1)
		else:
			print(min(remainingChocolates, noOfPoepleWithBaseNoOfChocolates)*2)
	else:
		peopleWithNoChocolates = noOfPeople - noOfChocolates 
		if peopleWithNoChocolates == noOfChocolates:
			print(noOfChocolates*2 - 1)
		else:
			print(min(peopleWithNoChocolates, noOfChocolates)*2)
	