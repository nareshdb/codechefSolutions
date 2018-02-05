t = input()


for x in range(0, t):

	s = raw_input()

	counts = [[] for a in range(26)]

	abccount = [0] * 26

	for y in range(0, len(s)):
		counts[ord(s[y])%26].append(y)
		abccount[ord(s[y])%26] += 1

	flag = 0
	for z in abccount:
		if z % 2 == 1:
			if len(s) % 2 == 0:
				flag = 2
				break
			elif flag == 1:
				flag = 2
				break
			else:
				flag = 1
	
	ans = [0] * len(s)

	if flag == 2:
		print(-1)
		continue
	else:
		start = 0
		limit = len(s) - 1
		for y in counts:
			if len(y) == 1:
				ans[len(s)/2] = y[0] + 1
			else:
				ylength = len(y)
				for z in range(0, ylength):
					if z < ylength/2:
						ans[start] = y[z] + 1
						start += 1
					else:
						ans[limit] = y[z] + 1
						limit -= 1

	print(' '.join(map(str, ans)))

