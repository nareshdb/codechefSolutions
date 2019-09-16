import math 

t = input()

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

for x in xrange(0, t):
	N, K = map(int, raw_input().split())
	A = map(int, raw_input().split())
	ans = 1
	sum = 0
	currentSeqMax = A[0]
	subSeq = []
	for i in range(0, N):
		if len(subSeq) < K:
			subSeq.append(A[i])
			if(currentSeqMax < A[i]):
				currentSeqMax = A[i]
			sum += A[i]
			continue
		elif A[i] < currentSeqMax:
			subSeq.remove(currentSeqMax)
			subSeq.append(A[i])
			sum -= currentSeqMax
			currentSeqMax = max(subSeq)
			sum += A[i]
		elif A[i] in subSeq:
			ans += 1
	subCountForMax = subSeq.count(currentSeqMax)
	totalCountForMax = A.count(currentSeqMax)
	print(nCr(totalCountForMax, subCountForMax))