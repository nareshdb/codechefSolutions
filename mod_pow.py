#compute mod power of x^y % m
def mod_pow(x, y, m):
	res = 1
	x = x % m
	while y > 0:
		if y & 1:
			res = (res * x) % m
		y = y >> 1
		x = (x*x) % m
	return int(res)
