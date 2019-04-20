noOfTestCases = input()

for i in range(0, noOfTestCases):
		
	noOfJobs, noOfJobsCompleted = map(int, raw_input().split())
	jobsCompleted = map(int, raw_input().split())
	jobs = [False] * noOfJobs
	for j in jobsCompleted:
		jobs[j-1] = True
	isChefsTurn = True
	chefsJobs = []
	assistantsJobs = []
	for j in range(0, len(jobs)):
		if not jobs[j]:
			if isChefsTurn:
				chefsJobs.append(str(j+1))
			else:
				assistantsJobs.append(str(j+1))
			isChefsTurn = not isChefsTurn
	print(" ".join(chefsJobs))
	print(" ".join(assistantsJobs))

