
def dfs(grid, ansgrid, i, j, num, m, n):

	if num <= 0:
		return

	num -= 1

	#right
	if (j+1 < m) and ansgrid[i][j+1] != 'B':
		ansgrid[i][j+1] = 'Y'
		dfs(grid, ansgrid, i, j+1, num, m, n)

	#left
	if (j-1 >= 0) and ansgrid[i][j-1] != 'B':
		ansgrid[i][j-1] = 'Y'
		dfs(grid, ansgrid, i, j-1, num, m, n)

	#top
	if (i+1 < n) and ansgrid[i+1][j] != 'B':
		ansgrid[i+1][j] = 'Y'
		dfs(grid, ansgrid, i+1, j, num, m, n)

	#bottom
	if (i-1 >= 0) and ansgrid[i-1][j] != 'B':
		ansgrid[i-1][j] = 'Y'
		dfs(grid, ansgrid, i-1, j, num, m, n)
    

#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	n, m = map(int, raw_input().split())

	grid = []
	ansgrid = []

	for i in range(0, n):
		grid.append(map(int, raw_input().split()))
		ansgridlist = []
		for j in range(0, m):
			if grid[i][j] == -1:
				ansgridlist.append('B')
			elif grid[i][j] == 0:
				ansgridlist.append('N')
			else:
				ansgridlist.append('Y')
		ansgrid.append(ansgridlist)


	for i in range(0, n):
		for j in range(0, m):
			if grid[i][j] > 0:
				dfs(grid, ansgrid, i, j, grid[i][j], m, n)

	for i in range(0, n):
			print(''.join(ansgrid[i]))














