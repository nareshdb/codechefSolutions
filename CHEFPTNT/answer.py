import math

#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	noOfPatents, monthsOfYear, workersBandwidth, totalWorkers = map(int, raw_input().split())

	s = str(raw_input())

	evenCount = 0
	oddCount = 0

	for i in s:
		if i == 'E':
			evenCount += 1
		else:
			oddCount += 1

	if (monthsOfYear == 0) or (workersBandwidth == 0) or (noOfPatents > totalWorkers):
		print("no\n")
		continue

	noOfEvenMonths = monthsOfYear/2
	noOfOddMonths = math.ceil(float(monthsOfYear)/2.0)

#	print("noOfEvenMonths" + str(noOfEvenMonths), "noOfOddMonths" + str(noOfOddMonths), "workersBandwidth" + str(workersBandwidth), "evenCount" + str(evenCount), "oddCount" + str(oddCount))

	if noOfPatents <= (min((noOfEvenMonths * workersBandwidth), evenCount) + min((noOfOddMonths * workersBandwidth), oddCount)):
		print("yes\n")
	else:
		print("no\n")