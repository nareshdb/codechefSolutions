t = input()

for x in xrange(0, t):

	s = raw_input()

	numberOf0s = 0

	for c in s:
		if c == '1':
			numberOf1s += 1

	print("LOSE" if numberOf1s % 2 == 0 else "WIN")