""" 
Each new term in the Fibonacci sequence is generated by adding the previous
two terms.  By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

import operator

def fibgen(max=4000000):
    """
    a memoizing generator
    """
    n = p1 = p2 = 0

    while n < max:
        if n < 1:
            n = 1
        else:
            n = p1 + p2

        p2 = p1
        p1 = n
        yield n

    raise StopIteration

def even(x):
    return not x % 2

def solve(max):
    return reduce(operator.add, [x for x in fibgen(max) if even(x)])

if __name__ == '__main__':
    
    # test
    f = fibgen()
    a = []
    
    # Starting with 1 and 2 ...
    f.next()
    while len(a) < 10:
        a.append(f.next())
    assert(a == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    print solve(4000000)


