#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	M, N = map(int, raw_input().split())

	Rx, Ry = map(int, raw_input().split())

	nMoves = input()

	moves = str(raw_input())

	originX = originY = 0

	for i in range(0,nMoves):
		if moves[i] == 'U':
			originY += 1
		elif moves[i] == 'D':
			originY -= 1
		elif moves[i] == 'R':
			originX += 1
		elif moves[i] == 'L':
			originX -= 1

	ans = "Case " + str(x+1) + ": "
	if ((originX > M) or (originY > N) or (originY < 0) or (originX < 0)):
		ans += "DANGER"
	elif originX == Rx and originY == Ry:
		ans += "REACHED"
	else: 
		ans += "SOMEWHERE"

	print(ans)