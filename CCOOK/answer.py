t = input()

for x in range(0, t):
	A = map(int, raw_input().split())
	ans = sum(A)

	if ans == 0:
		print("Beginner")
	elif ans == 1:
		print("Junior Developer")
	elif ans == 2:
		print("Middle Developer")
	elif ans == 3:
		print("Senior Developer")
	elif ans == 4:
		print("Hacker")
	elif ans == 5:
		print("Jeff Dean")
	