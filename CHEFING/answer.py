noOfTestCases = input()

for i in range(0, noOfTestCases):

	noOfDishes = input()
	charCount = {}

	for j in range(0, noOfDishes):
		ingredients = raw_input()
		presentChars = {}
		for k in range(0, len(ingredients)):
			presentChars[ingredients[k]] = True
		for ingredient, value in presentChars.items():
			if ingredient in charCount:
				charCount[ingredient] += 1
			else:
				charCount[ingredient] = 1
	answer = 0
	for ingredient, ingredientCount in charCount.items():
		if(ingredientCount == noOfDishes):
			answer += 1

	print(answer)

