import math
noOfTestCases = input()

def compareMatrix(matrix, comparisonMatrix, matSize):
	
	for j in range(0, int(math.ceil(float(matSize)/2.0))):
		
		noInJthCircleInitialMatrix = {}

		for l in range(j, matSize-j):
			noInJthCircleInitialMatrix[matrix[j][l]] = True
			noInJthCircleInitialMatrix[matrix[l][j]] = True
			noInJthCircleInitialMatrix[matrix[l][matSize-1-j]] = True
			noInJthCircleInitialMatrix[matrix[matSize-1-j][l]] = True

		for l in range(j, matSize-j):
			if (not comparisonMatrix[j][l] in noInJthCircleInitialMatrix) or (not comparisonMatrix[l][j] in noInJthCircleInitialMatrix) or (not comparisonMatrix[l][matSize-1-j] in noInJthCircleInitialMatrix) or (not comparisonMatrix[matSize-1-j][l] in noInJthCircleInitialMatrix):
				return False
	return True
			
for i in range(0, noOfTestCases):
	
	matSize = input()

	initialMatrix = []

	for j in range(0, matSize):
		jThRow = map(int, raw_input().split())
		initialMatrix.append(jThRow)

	finalMatrix = []
	for j in range(0, matSize):
		jThRow = map(int, raw_input().split())
		finalMatrix.append(jThRow)

	if compareMatrix(initialMatrix, finalMatrix, matSize):
		print("YES")	
	else:
		print("NO")