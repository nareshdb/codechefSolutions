noOfTestCases = input()

for n in range(0, noOfTestCases):
	answerChecks = 0
	wordsArray = map(str, raw_input().split())
	if "not" in wordsArray:
		print("Real Fancy")
	else:
		print("regularly fancy")
		