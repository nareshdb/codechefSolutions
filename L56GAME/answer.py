#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	n = raw_input()

	numbers = map(int, raw_input().split())

	odd = 0
	even = 0

	for i in range(0, len(numbers)):
		if numbers[i] % 2 == 1:
			odd += 1
		else:
			even += 1

	ans = 0

	if even > 0 or odd > 0:
		ans += 1
	if odd % 2 == 1:
			ans += 1

	print(ans)



