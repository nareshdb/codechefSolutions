#Number of test cases
nTestCases = input()

#Loop through all the test cases
for x in range(0, nTestCases):

	s = raw_input()

	ans = 0

	cCount = 0
	hCount = 0
	eCount = 0
	fCount = 0

	for i in range(0, len(s)):


		if i > 3:
			excluded = s[i-4]
			if excluded == 'c':
				cCount -= 1
			elif excluded == 'h':
				hCount -= 1
			elif excluded == 'e':
				eCount -= 1
			elif excluded == 'f':
				fCount -= 1  
				

		if s[i] == 'c':
			cCount += 1
		elif s[i] == 'h':
			hCount += 1
		elif s[i] == 'e':
			eCount += 1
		elif s[i] == 'f':
			fCount += 1

		if cCount == 1 and hCount == 1 and eCount == 1 and fCount == 1:
			ans += 1

	if ans == 0:
		print("normal")
		continue
	else:
		print("lovely " + str(ans))