import math
import time

def gcd(x, y): 
	while(y):
		x, y = y, x % y 
	return x 

def modInverse(b,m): 
	g = gcd(b, m)
	if (g != 1):
		return -1
	else:  
		# If b and m are relatively prime,  
		# then modulo inverse is b^(m-2) mode m  
		return pow(b, m - 2, m) 
  
  
# Function to compute a/b under modulo m  
def modDivide(a,b,m): 
	a = a % m 
	inv = modInverse(b,m) 
	if(inv == -1): 
		print("Division not defined") 
	else: 
		print("Result of Division is ",(inv*a) % m) 

def factmod(n, p):
	res = 1
	while n > 1:
		res = (res * (p-1 if (n/p) % 2 else 1)) % p
		for i in range(2, (n%p)+1):
			res = (res * i) % p
		n /= p
	return res % p

def f(n):
	ans = 1
	for i in range(2, n+1):
		ans = modDivide(ans, i, 1000000007)
	return ans

def nCr(n,r):
	return factmod(n, 1000000007) / factmod(r, 1000000007) / factmod(n-r, 1000000007)


# 	5 3
# 2 2 3 3 5
start = time.time()
N, K = map(int, raw_input().split())
primeNumbers = map(int, raw_input().split())

start = time.time()
primeNumbersCounts = [0]*8001

for p in primeNumbers:
	primeNumbersCounts[p+1] += 1

countsForK = [0]*(K+1)
countsForK[0] = 1

c = 0
for count in primeNumbersCounts:
	if count > 0:
	    for i in range(min(8000, K), 0, -1):
	    	c += 1
	    	#print("array is", countsForK)
	        countsForK[i] = countsForK[i] + (countsForK[i-1] * count)

print(sum(countsForK)%1000000007)