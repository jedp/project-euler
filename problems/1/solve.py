"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6, and 9.  The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 100.
"""

import operator

def has_multiple_in(n, multiples):
    for m in multiples:
        if n % m == 0:
            return True
    return False

def solve(r):
    return reduce(operator.add, [x for x in range(r) if has_multiple_in(x, [3, 5])])

if __name__ == '__main__':
    assert(solve(10) == 23)
    print solve(1000)
