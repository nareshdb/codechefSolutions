noOfTestCases = input()

for i in range(0, noOfTestCases):
	noOfSoldiers = input()
	attackPowersOfSoldiers = map(int, raw_input().split())
	defencePowersOfSoldiers = map(int, raw_input().split())
	
	maxAttackValues = []

	for j in range(0, noOfSoldiers):
		if (j == 0):
			maxAttackValues.append(attackPowersOfSoldiers[1]+attackPowersOfSoldiers[noOfSoldiers-1])
		elif (j == (noOfSoldiers - 1)):
			maxAttackValues.append(attackPowersOfSoldiers[noOfSoldiers-2] + attackPowersOfSoldiers[0])
		else:
			maxAttackValues.append(attackPowersOfSoldiers[j-1] + attackPowersOfSoldiers[j+1])
	
	answer = -1
	for j in range(0, noOfSoldiers):
		if(maxAttackValues[j] < defencePowersOfSoldiers[j]):
			answer = max(defencePowersOfSoldiers[j], answer)
	
	print(answer)
