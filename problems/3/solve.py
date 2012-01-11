"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import array
import math

def sieve(n):
    """
    Eratosthenes sieve
    """
    a = array.array('i')
    a.fromlist([1 for x in range(n)])

    a[0] = 0    # 1 isn't prime

    # p = 2 .. n
    for p in range(n+1)[2:]:
        while p*p < n:
            j = p*p
            while j < n:
                a[j] = 0
                j = j + p
            
            # skip to the next starting prime
            p += 1
            while p < n and a[p] == 0:
                p += 1

    # now convert to list of numbers
    primes = [p for p in range(len(a)) if a[p]]

    print "found", len(primes), "primes from 1 to", n
    return primes

def factor(n):
    primes = sieve(int(math.floor(math.sqrt(n))))
    factors = {}
    for p in primes[2:]:
        while n > 1 and not n % p:
            factors[p] = factors.get(p, 0) + 1
            n = n / p

    return sorted(factors.keys())


if __name__ == '__main__':
    print "assertion: prime factors of 13195 are 5, 7, 13, and 29"
    assert(factor(13195) == [5, 7, 13, 29])

    print "chug chug ..."
    n = 600851475143
    factors = factor(n)
    print "largest prime factor of", n, "is", factors[-1]


    
    

