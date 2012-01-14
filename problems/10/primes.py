import time
import itertools

def wheel2357():
    """
    Simple wheel generator for 2, 3, 5, and 7

    Yields 13, 17, 19, 23, ...
    """

    wheel = [2, 4, 2, 4, 6, 2, 6, 4,
             2, 4, 6, 6, 2, 6, 4, 2,
             6, 4, 6, 8, 4, 2, 4, 2, 
             4, 8, 6, 4, 6, 2, 4, 6, 
             2, 6, 6, 4, 2, 4, 6, 2, 
             6, 4, 2, 4, 2, 10, 2, 10]

    i = 0
    p = 11
    l = len(wheel)
    while True:
        p += wheel[i]
        yield p

        i = (i + 1) % l

def primegen():
    """
    Prime number sieve

    Yields 2, 3, 5, 7, ...
    """
    wheel = wheel2357()

    # initial set of primes assumed by our wheel
    for p in [2, 3, 5, 7, 11]:
        yield p

    ps = {}
    
    # next multiple not in wheel is of 11
    ps[121] = set([11])

    while True:
        p = wheel.next()

        if p in ps:
            # ps is a multiple of some prior prime
            # adjust the next multiples dictionary
            for fac in ps[p]:
                nextkey = fac + p
                if nextkey not in ps:
                    s = set()
                else:
                    s = ps[nextkey]
                s.add(fac)
                ps[nextkey] = s

        else:
            # p is prime
            yield p

        # for expected multiples we've passed, add to them
        # and push them into THE FUTURE!!!
        ps[p*p] = set([p])

        for key in [k for k in ps if k < p]:
            for fac in ps[key]:
                nextkey = key
                while nextkey < p:
                    nextkey += fac
                if nextkey not in ps:
                    s = set()
                else:
                    s = ps[nextkey]
                s.add(fac)
                ps[nextkey] = s

            del ps[key]
                

def takeprimes(n):
    s = time.time()
    l = list(itertools.islice(primegen(), n))
    e = time.time()
    print "got", n, "primes in", e-s, "sec"
    return l

if __name__ == '__main__':
    print "Assert 10001st prime == 104743"
    assert(takeprimes(10001)[-1] == 104743)

