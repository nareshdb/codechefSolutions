noOfTestCases = input()

for n in range(0, noOfTestCases):
	m, n = map(int, raw_input().split())
	if m%2==1 or n%2==1:
		print("NO")
		continue
	print("YES")

