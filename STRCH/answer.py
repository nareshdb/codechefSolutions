def noOfSubstrings(s):
	N = len(s)
	return ((N * (N+1)) / 2)

testCases = int(raw_input())

for i in range(0, testCases):

	N = int(raw_input())

	inputString, X = map(str, raw_input().split(" "))

	substrings = inputString.split(X)

	while '' in substrings:
		substrings.remove('')

	noOfIndependentStrings = 0

	for s in substrings:
		noOfIndependentStrings += noOfSubstrings(s)

	print(noOfSubstrings(inputString) - noOfIndependentStrings)