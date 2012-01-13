"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import operator
import primes

def solve(n):
    s = 0
    p = 0
    ps = primes.primegen()
    while p < n:
        s += p
        p = ps.next()
    return s

if __name__ == '__main__':
    print "Sum of primes below 10 is 17"
    assert(solve(10) == 17)
