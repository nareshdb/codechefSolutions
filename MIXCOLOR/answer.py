t = input()

for x in range(0, t):

	N = int(raw_input())

	A = map(int, raw_input().split())

	occurenceDict = {}

	for i in range(0, len(A)):
		if occurenceDict.get(A[i]) == None:
			occurenceDict[A[i]] = 1
		else:
			occurenceDict[A[i]] += 1

	ans = 0

	for key, value in occurenceDict.iteritems():
		if value > 1:
			ans += (value-1)

	print(ans)