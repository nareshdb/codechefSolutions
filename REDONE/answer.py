t = input()

reducedIntFor = {1:1}
maxReduced = 1

for x in range(0, t):
	
	numberToReduce = input()

	if numberToReduce > maxReduced:
		for y in range(maxReduced + 1, numberToReduce+1):
			reducedInt = y * reducedIntFor[y-1] + y + reducedIntFor[y-1]
			if reducedInt > 1000000007:
				reducedInt %= 1000000007
			reducedIntFor[y] = reducedInt
			maxReduced = y

	print(reducedIntFor[numberToReduce])		


	
