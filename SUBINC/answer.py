t = input()

for x in range(0, t):
	N = int(raw_input())
	A = map(int, raw_input().split())
	B = [1]
	ans = 0
	for i in range(1, N):
		if A[i-1] <= A[i]:
			B.append(B[i-1]+1)
		else:
			B.append(1)
	print(sum(B))
