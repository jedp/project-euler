"""
A palindromic number reads the same both ways.  The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers
"""

import types

def string_is_palindrome(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return string_is_palindrome(s[1:-1])

def number_is_palindrome(n):
    return string_is_palindrome(str(n))

def solve(digits):
    assert(digits >= 2)
    top = pow(10, digits)
    bot = pow(10, digits - 1)
    greatest = (0, 0, 0)

    I = J = 0

    for i in range(top - bot):
        I = i + bot 
        for j in range(top - bot - i):
            J = j + I 
            if number_is_palindrome(I * J):
                if I*J > greatest[0] * greatest[1]:
                    greatest = I, J
                    print I, J, '->', I*J

    return greatest

if __name__ == '__main__':
    assert(number_is_palindrome(1))
    assert(number_is_palindrome(11))
    assert(number_is_palindrome(111))
    assert(number_is_palindrome(121))
    assert(number_is_palindrome(123321))

    print "Assert 9009 is palindrome"
    assert(number_is_palindrome(9009))

    print "Assert (91, 99) is best solution for two digits"
    assert(sorted(list(solve(2))) == [91, 99])

    print "Solve largest palindrome for three-digit numbers"
    result = solve(3)
    print result, '->', result[0]*result[1]

