noOfTestCases = input()

for i in range(0, noOfTestCases):
	noOfChefs = input()
	noOfJarsRequiredArray = map(int, raw_input().split())
	print(max(noOfJarsRequiredArray))
