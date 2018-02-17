t = input()

for x in range(0, t):
	N = int(raw_input())
	A = map(int, raw_input().split())
	C, D, S = map(int, raw_input().split())
	print(max(A) * (C - 1))