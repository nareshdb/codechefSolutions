#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	L, K = map(int, raw_input().split())

	n = L - K + 1

	ans = "Case " + str(x+1) + ": "

	if K<=L:
		ans += str((n*(n+1))/2)
	else:
		ans += "0"
	

	print(ans)