t = input()

for x in range(0, t):
	
	noOfDays = input()

	attendance = raw_input()

	noOfDaysPresent = 0
	noOfDaysRequired = 0

	for a in attendance:
			if a == 'P':
				noOfDaysPresent += 1

	if noOfDays > 4 and float(noOfDaysPresent+noOfDaysRequired)/float(noOfDays) < 0.75:
		for i in range(2, noOfDays-2):
			if attendance[i] == 'A' and ((attendance[i-1] == 'P' or attendance[i-2] == 'P') and (attendance[i+1] == 'P' or attendance[i+2] == 'P')):
				noOfDaysRequired += 1
			if float(noOfDaysPresent+noOfDaysRequired)/float(noOfDays) >= 0.75:
				break

	# print("noOfDaysRequired" + str(noOfDaysRequired))
	# print("noOfDaysPresent" + str(noOfDaysPresent))
	print({True: noOfDaysRequired, False: str(-1)} [float(noOfDaysPresent+noOfDaysRequired)/float(noOfDays) >= 0.75])