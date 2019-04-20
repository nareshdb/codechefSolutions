def checkFitting(a, b, n):
	for i in range(0, n):
		if a[i] > b[i]:
			return False
	return True

t = input()

for x in range(0, t):
	N = int(raw_input())
	A = map(int, raw_input().split())
	B = map(int, raw_input().split())

	left = checkFitting(A, B, N)
	right = checkFitting(list(reversed(A)), B, N)

	if left and right:
		print("both")
	elif left:
		print("front")
	elif right: 
		print("back")
	else: print("none")
