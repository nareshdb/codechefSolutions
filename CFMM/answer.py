t = input()

for x in range(0, t):
	
	noOfLines = input()
	
	dictOfChars = {}

	for y in range(0, noOfLines):
		line = raw_input()
		for l in line:
			if l in dictOfChars:
				dictOfChars[l] += 1
			else:
				dictOfChars[l] = 1

	ans = 0

	while True:
		codeChef = 'codechef'
		didWeFindIt = True
		for c in codeChef:
			if c not in dictOfChars:
				didWeFindIt = False
				break

		charCount = 0
		if didWeFindIt:
			for c in codeChef:
				countOfC = dictOfChars[c]
				if countOfC <= 0:
					break
				else:
					charCount += 1
					dictOfChars[c] = countOfC - 1

			if charCount == 8:
				ans += 1
			else:
				break
		else:
			break

	print(ans)