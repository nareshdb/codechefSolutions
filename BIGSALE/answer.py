t = input()

for x in range(0, t):
	
	N = int(raw_input())

	ans = 0.0

	for y in range(0, N):

		price, qty, disc = map(float, raw_input().split())

		if disc == 0:
			continue

		dummyPrice = (price + price*(disc/100))

		salePrice = dummyPrice - (dummyPrice*(disc/100))

		ans += (price - salePrice) * qty

	print(ans)
				
	