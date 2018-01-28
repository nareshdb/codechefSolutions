#Number of test cases
nTestCases = input()

#compute mod power of x^y % m
def mod_pow(x, y, m):
	res = 1
	x = x % m
	while y > 0:
		if y & 1:
			res = (res * x) % m
		y = y >> 1
		x = (x*x) % m
	return int(res)


#Loop through all the test cases
for x in range(0, nTestCases):

	n, m = map(int, raw_input().split())

	print "Case %d:"%(x+1)

	for i in range(0, m):
		s = raw_input()
		if n < len(s):
			print(0)
			continue
		print((mod_pow(26, n - len(s), 1000000007) * (n - len(s) + 1)) % (1000000007))