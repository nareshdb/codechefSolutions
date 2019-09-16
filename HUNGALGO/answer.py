t = input()

for x in range(0, t):
	
	sizeOfMatrix = input()
	
	matrix = []

	noOfZerosInRows = 0
	noOfZerosInColumns = 0

	for y in range(0, sizeOfMatrix):
		matrix.append([])
		matrix[y] = map(int, raw_input().split())

		if 0 in matrix[y]:
			noOfZerosInRows += 1

	for y in range(0, sizeOfMatrix):
		array = []
		for z in range(0, sizeOfMatrix):
			array.append(matrix[z][y])
		
		if 0 in array:
			noOfZerosInColumns += 1

	if noOfZerosInRows >= sizeOfMatrix and noOfZerosInColumns >= sizeOfMatrix:
		print("YES")
	else:
		print("NO")
