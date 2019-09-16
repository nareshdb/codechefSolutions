def numberOfEqualXORSubarrays(arrayOfNumbers, lengthOfArray):
    return lengthOfArray-1
        

def numOfSubarraysWithXOR(lengthOfArray, arrayOfNumbers, xorToFind):
    
    prevXors = dict()
    indexes = dict()
    xors = [0]*lengthOfArray
    xors[0] = arrayOfNumbers[0]
    
    for i in xrange(1, lengthOfArray):
        xors[i] = xors[i - 1] ^ arrayOfNumbers[i]

    #print("xors " + str(xors))

    countOfXors = 0
    
    for i in xrange(0, lengthOfArray):
        xor = xorToFind ^ xors[i]

        #print("calculated xor at this moment = " + str(xor))

        if xor in prevXors.keys():
            #print("got a hit in keys where i is " + str(i))
            #XOR from some previous matching indexes is 0, we need to process all those arrays to find matching XOR sub arrays
            
            for index in indexes[xor]:
                arr = xors[index+1:i+1]
                countOfXors += numberOfEqualXORSubarrays(arr, len(arr))
            
        if (xors[i] == xorToFind):
            #print("xor value is matchd whr i is " + str(i))
            arr = xors[0:i+1]
            countOfXors += numberOfEqualXORSubarrays(arr, len(arr))
            #XOR from the beginning of the array is 0, we need to look for equal value subarrays from [0...i]

        
        if not xor in indexes.keys():
            #print("creting for " + str(i))
            indexes[xor] = list([i])
        else:
            #print("adding for " + str(i))
            indexes[xor].append(i)

        prevXors[xors[i]] = prevXors.get(xors[i], 0) + 1

    #print("prevXors " + str(prevXors))

    #print("indexes" + str(indexes))

    return countOfXors

t = input()

for x in xrange(0, t):

    lengthOfTestCaseArray = input()

    tArray = map(int, raw_input().split())

    numberOfArraysWithXOR0 = numOfSubarraysWithXOR(lengthOfTestCaseArray, tArray, 0)

    print(numberOfArraysWithXOR0)