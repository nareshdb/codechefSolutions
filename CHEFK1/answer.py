import math
import time

def gcd(x, y): 
	while(y):
		x, y = y, x % y 
	return x 

def fact(n):
	ans = 1
	for i in range(2, n+1):
		ans = ans*i
	return ans

def nCr(n,r):
	return fact(n) / fact(r) / fact(n-r)

t = input()

for i range(0, t):

	N, M = map(int, raw_input().split())
	
	minimumEdges = N-1
	maximumEdges = nCr(N, 2)+N

	if M < minimumEdges or M > maximumEdges:
		print("-1")
		continue

	