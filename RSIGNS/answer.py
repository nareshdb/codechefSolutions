import math 
  
t = input()

def intpow(base, exp):
   if exp == 0:
      return 1
   elif exp == 1:
      return base
   elif (exp & 1) != 0:
       return base * intpow(base * base, exp // 2)
   else:
       return intpow(base * base, exp // 2)

for x in xrange(0, t):

	n = input()
	ans = intpow(2, n)
	modNum = 10**9 + 7

	# for y in range(0, n):
	# 	ans = (ans << 1) % modNum

	ans = (ans * 5) % modNum
	print(ans)