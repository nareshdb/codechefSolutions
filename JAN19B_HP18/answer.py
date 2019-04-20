import math

noOfTestCases = input()

for i in range(0, noOfTestCases):

	inputLine1 = raw_input()
	inputLine2 = raw_input()
	sizeOfTheArray, bobsNumber, alicesNumber = map(int, inputLine1.split())
	numbersArray = map(int, inputLine2.split())

	noOfBobsNumbers = 0
	noOfAlicesNumbers = 0
	commonNumbers = 0

	for n in numbersArray:
		if (n%bobsNumber == 0) and (n%alicesNumber == 0):
			commonNumbers += 1
		elif n%bobsNumber == 0:
			noOfBobsNumbers += 1
		elif n%alicesNumber == 0:
			noOfAlicesNumbers += 1

	if noOfBobsNumbers + (math.ceil(commonNumbers/2)) <= noOfAlicesNumbers:
		print("ALICE")
	else:
		print("BOB")