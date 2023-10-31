from math import isqrt
from random import randint, randrange
class Compute_Primes:
    def __init__(self) -> None:
        self.p = int
        self.q = int

    def is_Prime(self, n):
        """
        Miller-Rabin primality test.

        A return value of False means n is certainly not prime. A return value of
        True means n is very likely a prime.
        """
        if n!=int(n):
            return False
        n=int(n)
        #Miller-Rabin test for prime
        if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
            return False
            
        if n==2 or n==3 or n==5 or n==7:
            return True
        s = 0
        d = n-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == n-1)
    
        def trial_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True  
    
        for i in range(8):#number of trials 
            a = randrange(2, n)
            if trial_composite(a):
                return False
    
        return True

    
    def exponentiating(self, n, e) -> int:
        if n % 2 == 0:
            return n ** (2 * e // 2)
        else:
            return n * (n** (2* ((e-1) // 2)))
    
    def create_primes(self) -> int:
        while True:
            b = 2**1023
            c = 2**1024 - 1
            a = randint(b, c)
            # a = randint(self.exponentiating(2, 1023), self.exponentiating(2, 1024) - 1)
            print(a)
            if self.is_Prime(a) is True:
                print('yo')
                return a



    
primes = Compute_Primes()
print(f"Prime number is: {primes.create_primes()}")