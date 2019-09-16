t = input()

for x in xrange(0, t):

	caveLength = input()
	caveRadiations = map(int, raw_input().split())
	zombieHealths = map(int, raw_input().split())
	
	additions = [0]*caveLength
	deletions = [0]*caveLength
	
	for iRad in xrange(0, caveLength):
		additions[max(0, iRad-caveRadiations[iRad])] += 1
		deletions[min(caveLength-1, iRad+caveRadiations[iRad])] -= 1
		
	finalCaveRadiations = [0]*caveLength
	currentRadiation = additions[0]
	finalCaveRadiations[0] = currentRadiation

	#print(additions)
	#print(deletions)

	for i in range(1, caveLength):
		print(finalCaveRadiations)
		currentRadiation += additions[i]
		finalCaveRadiations[i] = currentRadiation
		currentRadiation += deletions[i]

	#print(finalCaveRadiations)

	print("YES" if sorted(finalCaveRadiations) == sorted(zombieHealths) else "NO")