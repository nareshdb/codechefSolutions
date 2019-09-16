t = input()

for x in range(0, t):
	
	noOfPoints = input()

	positiveSlopeConstants = []
	negativeSlopesConstants = []

	for y in range(0, noOfPoints):
		px, py = map(int, raw_input().split())
		positiveSlopeConstants.append(py - (1 * px))
		negativeSlopesConstants.append(py - (-1 * px))
		
	positiveSlopeConstants.sort()
	negativeSlopesConstants.sort()

	#finding minimum distance pair of positive slope pairs
	minDistanceOfPositiveSlopes = abs(positiveSlopeConstants[0] - positiveSlopeConstants[1])

	for y in range(2, len(positiveSlopeConstants)):
		if(abs(positiveSlopeConstants[y] - positiveSlopeConstants[y-1])<minDistanceOfPositiveSlopes):
			minDistanceOfPositiveSlopes = abs(positiveSlopeConstants[y] - positiveSlopeConstants[y-1])

	#finding minimum distance pair of negative slope pairs
	minDistanceOfNegativeSlopes = abs(negativeSlopesConstants[0] - negativeSlopesConstants[1])

	for y in range(2, len(negativeSlopesConstants)):
		if(abs(negativeSlopesConstants[y] - negativeSlopesConstants[y-1])<minDistanceOfNegativeSlopes):
			minDistanceOfNegativeSlopes = abs(negativeSlopesConstants[y] - negativeSlopesConstants[y-1])

	print(positiveSlopeConstants)
	print(negativeSlopesConstants)

	if(minDistanceOfPositiveSlopes < minDistanceOfNegativeSlopes):
		print(float(minDistanceOfPositiveSlopes)/2.0)
	else:
		print(float(minDistanceOfNegativeSlopes)/2.0)