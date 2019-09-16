import math 
  
t = input()


def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x  
      

for x in xrange(0, t):

	length = input()

	numbers = map(int, raw_input().split())

	numbers = set(numbers)

	numbers = list(numbers)

	numbers.sort()

	length = len(numbers)

	largest = numbers[length-1]
	gcd1 = largest

	gcd2 = largest
	if length>1:
		gcd2 = numbers[0]

	if len(numbers) >= 2:

		if numbers[length-2] > largest/2:
			largest = numbers[length-2]

		numbers.remove(largest)

		gcd1 = largest
		num1 = numbers[0] 
		num2 = numbers[1]

		gcd2 = find_gcd(num1, num2)

		for i in range(2, len(numbers)):
			if gcd2 > numbers[i]:
				gcd2 = find_gcd(numbers[i], gcd2)
   			else:
   				gcd2 = find_gcd(gcd2, numbers[i])

   	print(gcd1 + gcd2)