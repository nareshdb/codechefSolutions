#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	n, m = map(int, raw_input().split())

	print("Case " + str(x+1) + ":")

	for i in range(0, m):
		s = raw_input()
		magicnum = n - len(s)
		exp26 = 1
		for j in range(0, magicnum):
			exp26 = (exp26 * 26) % 1000000007
		print(((exp26) * (magicnum + 1)) % (1000000007))
		
