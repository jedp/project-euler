"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

import math
import itertools

def primegen():
    """
    horridly brute-force
    """
    p = 1
    lastp = 2

    while True:
        p += 1

        while True:
            for i in xrange(lastp, int(math.floor(math.sqrt(p))) + 1):
                if not p % i:
                    p += 1
                    break

            # when loop terminates
            else:
                break

        yield p
    

if __name__ == '__main__':
    print "Testing assertions ...",
    assert(list(itertools.islice(primegen(), 6)) == [2, 3, 5, 7, 11, 13])
    print "ok"

    n = 10001
    print "%dst prime number:" % (n),
    print list(itertools.islice(primegen(), n))[-1]
