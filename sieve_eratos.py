from __future__ import print_function
# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    return prime
  
# driver program 
if __name__=='__main__': 
    n = 1000000
    requiredThings = []
    primes = SieveOfEratosthenes(n)
    
    for i in range(0, len(primes)):
        if primes[i]:
            print(i**2)
            