"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

import math

def find_squares(max_root=1000):
    i = 1
    i2 = 1
    while i <= max_root:
        yield (i, i2)
        i += 1
        i2 = pow(i, 2)
    raise StopIteration

def solve(n):
    """
    Find the pythagorean triplet a,b,c for which a + b + c = n
    """
    roots = {}
    for root,square in find_squares(n):
        roots[root] = square

    b = c = n
    tries = 0
    # brute force
    for a in range(n+1)[1:]:
        c = n - a - 1
        b = 1000 - a - c
        while b < c and c > a:
            tries += 1
            c -= 1
            b = n - a - c
            if roots[a] + roots[b] == roots[c]:
                print "after", tries, "iterations"
                return a, b, c
        
"""
This is elegant:
Formula posted by Pier on projecteuler.net/?thread=9

a = 2mn
b = m^2 - n^2
c = m^2 + n^2
a + b + c + 1000

2mn + (m^2 - n^2) + (m^2 - n^2) = 1000
2mn + 2m^2 = 1000
2m(m+n) = 1000
m(m+n) = 500

m > n

m = 20
n = 5

a = 200, b = 375, c = 425

So pretty!
"""


if __name__ == '__main__':
    n = 1000
    a, b, c = solve(n)

    assert(a + b + c == n)
    
    print "%d^2 + %d^2 = %d^2  (%d + %d = %d)" % (a, b, c, pow(a,2), pow(b,2), pow(c,2))
    print "Product", a, "*", b, "*", c, "=", a*b*c


