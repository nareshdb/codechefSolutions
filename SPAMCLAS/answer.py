#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	#input for each test case, numOfLayers(numbers of layers, ie. number of neurons), minX, maxX
	numOfLayers, minX, maxX = map(int, raw_input().split())

	#[i][0] is Wi, [i][1] is Bi
	WiBi = []

	#take input for all the layers(or neurons as no._ofneurons = no._oflayers)
	for y in range(0, numOfLayers):
		WiBi.append([0 for _ in range(0,2)])
		WiBi[y][0], WiBi[y][1] = map(int, raw_input().split())
	
	#2 values to store for odd or even
	val = [0,0]

	for x in range(0,2):
		res = x
		for i in range(0, numOfLayers):
			res = (res * WiBi[i][0] + WiBi[i][1]) % 2
		val[x] = res;
	
	#count for even
	even = 0

	if val[minX % 2] == 0:
		even += (maxX - minX) / 2 + 1;
	
	if (val[(minX + 1) % 2] == 0):
		even += (maxX - minX - 1) / 2 + 1;

	odd = maxX - minX + 1 - even

	ans = str(even) + ' ' + str(odd)

	print(ans)