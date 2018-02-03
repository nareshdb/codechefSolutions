#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	totalTopics = int(raw_input())

	days = map(int, raw_input().split())

	sumOfTopics = int(sum(days))

	ans = 0

	if sumOfTopics < totalTopics:
		totalTopics = totalTopics % sumOfTopics
		for x in range(0, 7):
			if days[x] > 0:
				ans = x

	if totalTopics > 0:
		for i in range(0, 7):
			totalTopics -= days[i]
			if totalTopics <= 0:
				ans = i
				break
	

	if ans == 0:
		print('Monday')
	elif ans == 1:
		print('Tuesday')
	elif ans == 2:
		print('Wednesday')
	elif ans == 3:
		print('Thursday')
	elif ans == 4:
		print('Friday')
	elif ans == 5:
		print('Saturday')
	elif ans == 6:
		print('Sunday')