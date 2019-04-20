noOfTestCases = input()

			
for i in range(0, noOfTestCases):
	
	r, c, k = map(int, raw_input().split())
	chessBoard = [[False] * 8 for i in range(8)]
	
	ans = 0
	for j in range(0, 8):
		for _k in range(0, 8):
			dist = max(abs(r-1 - j), abs(c-1 - _k))
			if dist<=k:
				ans += 1
	print(ans)
