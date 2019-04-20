lengthOfFirstArray, lengthOfSecondArray = map(int, raw_input().split())

firstArray = map(int, raw_input().split())
secondArray = map(int, raw_input().split())

sumDictionary = {}

for i in range(0, lengthOfFirstArray):
	for j in range(0, lengthOfSecondArray):
		sumDictionary[firstArray[i] + secondArray[j]] = [i, j]
		if len(sumDictionary) == (lengthOfSecondArray + lengthOfFirstArray - 1):
			break

	if len(sumDictionary) == (lengthOfSecondArray + lengthOfFirstArray - 1):
		break

for pair in sumDictionary:
	print(str(sumDictionary[pair][0]) + ' ' + str(sumDictionary[pair][1]))