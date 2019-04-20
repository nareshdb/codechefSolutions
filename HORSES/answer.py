noOfTestCases = input()

for i in range(0, noOfTestCases):
	noOfHorses = input()
	horses = map(int, raw_input().split())
	horses.sort()
	min = abs(horses[0] - horses[1])
	for j in range(2, noOfHorses):
		if abs(horses[j] - horses[j-1]) < min:
			min = abs(horses[j] - horses[j-1])
	
	print(min)
	
