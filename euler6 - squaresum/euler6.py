__author__ = 'apothem'


'''
Project Euler problem 6: square and sum

6: The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def euler6():

    sumsquares = 0
    squaresum = 0

    for i in range (1, 101, 1):
        sumsquares += (i ** 2)
        squaresum += i

    squaresum ** 2

    return sumsquares - squaresum

print (euler6())
# 333300