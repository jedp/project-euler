"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Solution:

    The idea is to take the prime factors of each number x in 1..n, 
    and then multiply the largest factors together to get the result.

    For example, the prime factors of the numbers in 1..10 are:
         1 -> 1
         2 -> 2
         3 -> 3
         4 -> 2^2
         5 -> 5
         6 -> 2, 3
         7 -> 7
         8 -> 2^3
         9 -> 3^2
        10 -> 2, 5

    For the resulting factors, the largest are:

        1,
        2^3  (from 8)
        3^2  (from 9)
        5
        7

    So the result is

        1 + pow(2,3) * pow(3,2) * 5 * 7 = 2520
        
"""

import array
import math

def sieve(n):
    """
    Eratosthenes sieve
    """
    a = array.array('i')
    a.fromlist([1 for x in range(n+1)])

    a[0] = 0    # 1 isn't prime

    # p = 2 .. n
    for p in range(n+1)[2:]:
        while p*p < n:
            j = p*p
            while j <= n:
                a[j] = 0
                j = j + p
            
            # skip to the next starting prime
            p += 1
            while p <= n and a[p] == 0:
                p += 1

    # now convert to list of numbers
    primes = [p for p in range(len(a)) if a[p]]

    return primes

def factor(n):
    """
    Return prime factors of n
    """
    primes = sieve(n)
    factors = {n: 0}
    for p in primes[1:]:
        while n > 1 and not n % p:
            factors[p] = factors.get(p, 0) + 1
            n = n / p

    return factors

def accumulate_factors(n):
    """
    Accumulate largest prime factors for numbers 1..n
    """
    factors = {}
    for i in range(n+1)[1:]:
        f = factor(i)
        for k in f.keys():
            if f[k] > factors.get(k, 0):
                factors[k] = f[k]

    print "accum factors for", n, "are:", factors
    return factors

def solve(n):
    """
    Compute the smallest number that is evenly divisible by each of the
    numbers 1..n.
    """
    factors = accumulate_factors(n)
    accum = 1
    for k in factors:
        accum *= pow(k, factors[k])

    return accum


if __name__ == '__main__':
    print "Assert solve(10) == 2520"
    assert(solve(10) == 2520)

    print "Computing solve(20)"
    print solve(20)


