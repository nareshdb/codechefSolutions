noOfTestCases = input()

for i in range(0, noOfTestCases):
	
	N, A, B, K = map(int, raw_input().split())

	answer = 0	
	
	if (max(A,B)%min(A,B) == 0):
		answer += N/min(A,B)
		answer -= N/max(A,B)
	else:
		answer += N/A
		answer += N/B
		answer -= N/(A*B)

	if(answer >= K):
		print("Win")
	else:
		print("Lose")
		
