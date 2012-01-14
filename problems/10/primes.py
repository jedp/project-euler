import time
import heapq
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

    h = []
    
    # next multiple not in wheel is of 11
    heapq.heappush(h, (121, 11))

    while True:
        p = wheel.next()

        n, fac = heapq.heappop(h)

        if n > p:
            # factors skip past p, so p is prime.
            # put factors back into the future, 
            # along with p itself
            heapq.heappush(h, (n, fac))
            heapq.heappush(h, (p*p, p))

            yield p


        elif n == p:
            # p is a multiple of a prior prime

            while (not n % 2) or (not n % 3):
                n += fac
            heapq.heappush(h, (n, fac))

        else:
            # p factors are too small.  increment until
            # greater than p and push back into the future.

            while n < p:
                while n < p:
                    n += fac

                n, fac = heapq.heappushpop(h, (n, fac))
                
            # maybe we found a prime while doing that
            if n > p:
                yield p

            # the last one skipped p - push back
            heapq.heappush(h, (n, fac))


def takeprimes(n):
    s = time.time()
    l = list(itertools.islice(primegen(), n))
    e = time.time()
    print "got", n, "primes in", e-s, "sec"
    return l

if __name__ == '__main__':
    print "Assert 10001st prime == 104743"
    assert(takeprimes(10001)[-1] == 104743)

