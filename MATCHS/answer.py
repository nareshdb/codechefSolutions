t = input()



for x in range(0, t):
	
	N, M = map(int, raw_input().split())

	isAri = True

	while True:

		biggerOne = max(M, N)
		smallerOne = min(M, N)

		if biggerOne%smallerOne == 0 or biggerOne/smallerOne > 1:
			break

		N = biggerOne - smallerOne
		M = smallerOne

		isAri = not isAri

	if isAri:
		print("Ari")
	else:
		print("Rich")