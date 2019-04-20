noOfTestCases = input()


def leftPoint(x, y, size):
	if x == 1:
		return None
	return (x - 1, y)

def rightPoint(x, y, size):
	if x == size:
		return None
	return (x + 1, y)

def topPoint(x, y, size):
	if y == 1:
		return None
	return (x, y - 1)

def bottomPoint(x, y, size):
	if y == size:
		return None
	return (x, y + 1)



for n in range(0, noOfTestCases):
	
	N, M, noOfPlants = map(int, raw_input().split())

	isPlantThereAtXY = {}

	ans = 0

	for i in range(0, noOfPlants):
		x, y = map(int, raw_input().split())

		isPlantThereAtXY[(x, y)] = True

	for point in isPlantThereAtXY:

		print(point)

		x, y = point

		left = leftPoint(x, y, N)

		right = rightPoint(x, y, N)

		top = topPoint(x, y, M)

		bottom = bottomPoint(x, y, M)

		if left == None:
			ans += 1
		elif left != None:
			lx, ly = left
			if not (lx, ly) in isPlantThereAtXY:
				ans += 1


		if right == None:
			ans += 1
		elif right != None:
			rx, ry = right
			if not (rx, ry) in isPlantThereAtXY:
				ans += 1


		if top == None:
			ans += 1
		elif top != None:
			tx, ty = top
			if not (tx, ty) in isPlantThereAtXY:
				ans += 1


		if bottom == None:
			ans += 1
		elif bottom != None:
			bx, by = bottom
			if not (bx, by) in isPlantThereAtXY:
				ans += 1

	print(ans)