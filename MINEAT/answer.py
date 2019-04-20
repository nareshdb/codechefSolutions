import math

t = input()

for x in range(0, t):
	
	N, H = map(float, raw_input().split())

	A = map(float, raw_input().split())

	print(int(math.ceil(sum(A)/H)))
		

	