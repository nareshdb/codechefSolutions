import math 
  
t = input()

limit = 1000000007

for x in xrange(0, t):

  n, k = map(int, raw_input().split())
	
  noOfUnreachableNos = 0

  nthTerm = k-1

  nMinus1THTerm = max(k*2 - (k+n), 0)
  
  difference = nthTerm - nMinus1THTerm

  if difference == 0:
    noOfTerms = 1
  else:
    noOfTerms = int(math.ceil(float(nthTerm)/float(difference)))

  firstTerm = nthTerm - (noOfTerms-1) * (difference)

  noOfUnreachableNos = (noOfTerms * (firstTerm + nthTerm))/2


  # print("\nnthTerm = " + str(nthTerm)) 
  # print("nMinus1THTerm  = " + str(nMinus1THTerm))
  # print("firstTerm = " + str(firstTerm))
  # print("difference = " + str(difference))
  # print("noOfTerms = " + str(noOfTerms))
  

  print(noOfUnreachableNos % limit)  

  

  # 1 2 3 4 5 6 7 8 9 [10, 11, 12 ] 13, 14 15 16 17 18 19 [20, 21, 22, 23, 24] 25, 26, 27, 28, 29 [30, 31, 32, 33 34 35, 36] 37 38 29
  # 1 2 3 4 5 6 7 [8, 9, 10, 11] 12, 13, 14, 15 [16, 17, 18, 19, 20, 21, 22] 23 [24, 25, 26]
  # 1 2 3 4 [5] 6 7 8 9 [10] 11 12 13 14
  