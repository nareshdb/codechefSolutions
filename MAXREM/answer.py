testCases = raw_input()

inputArray = map(int, raw_input().split(" "))

inputArray = list(set(inputArray)) #removing duplicates

if len(inputArray) > 1:
    maximum = max(inputArray)
    inputArray.remove(maximum)
    print(max(inputArray))
else:
    print(0)
