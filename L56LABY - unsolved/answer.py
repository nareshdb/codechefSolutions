import heapq


def dfs(grid, i, j, num, m, n):

	num -= 1

	if num < 1:
		return

	#right
	if ((j+1 < m) and (grid[i][j+1] != -1) and ((grid[i][j+1] - 1) < grid[i][j])):
		grid[i][j+1] = num
		dfs(grid, i, j+1, num, m, n)

	#left
	if ((j-1 >= 0) and (grid[i][j-1] != -1) and ((grid[i][j-1] - 1) < grid[i][j])):
		grid[i][j-1] = num
		dfs(grid, i, j-1, num, m, n)

	#bottom
	if ((i-1 >= 0) and (grid[i-1][j] != -1) and ((grid[i-1][j] - 1) < grid[i][j])):
		grid[i-1][j] = num
		dfs(grid, i-1, j, num, m, n)

	#top
	if ((i+1 < n) and (grid[i+1][j] != -1) and ((grid[i+1][j] - 1) < grid[i][j])):
		grid[i+1][j] = num
		dfs(grid, i+1, j, num, m, n)
    

#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	n, m = map(int, raw_input().split())

	grid = []
	h = []

	for i in range(0, n):
		grid.append(map(int, raw_input().split()))
		ansgridlist = []
		for j in range(0, m):
			if grid[i][j] > 0:
				heapq.heappush(h, ((-1 * grid[i][j], i, j)))

	while h != []:
		elem = (heapq.heappop(h))
		val = elem[0]
		i = elem[1]
		j = elem[2]
		dfs(grid, i, j, -1 * val + 1, m, n)

	for i in range(0, n):
		for j in range(0, m):
			if grid[i][j] > 0:
				grid[i][j] = 'Y'
				continue
			elif grid[i][j] == -1:
				grid[i][j] = 'B'
				continue
			else: grid[i][j] = 'N'



	for i in range(0, n):
			print(''.join(grid[i]))














