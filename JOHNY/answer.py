noOfTestCases = input()

for i in range(0, noOfTestCases):
	noOfSongs = input()
	songsLengths = map(int, raw_input().split())
	indexOfUncleJohny = input()
	lengthOfUncleJohny = songsLengths[indexOfUncleJohny-1]
	futureIndexOfSong = 1
	for s in songsLengths:
		if s<lengthOfUncleJohny:
			futureIndexOfSong += 1
	print(futureIndexOfSong)

