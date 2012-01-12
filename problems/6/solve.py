"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import operator

def squares_summed(n):
    accum = 0
    for i in range(n+1)[1:]:
        accum += pow(i,2)

    return accum

def sum_squared(n):
    return(pow(reduce(operator.add, range(n+1)[1:]), 2))


if __name__ == '__main__':
    print "Testing assertions ...",
    assert(squares_summed(10) == 385)
    assert(sum_squared(10) == 3025)
    assert(sum_squared(10) - squares_summed(10) == 2640)
    print "ok"

    print "Squares summed of first 100 natural numbers:",
    a = squares_summed(100)
    print a
    
    print "Sum of squared of first 100 natural numbers:", 
    b = sum_squared(100)
    print b

    print "difference:",
    print b - a

