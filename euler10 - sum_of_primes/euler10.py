__author__ = 'apothem'


'''
Project Euler problem #10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

def is_prime(n):
    import math                                                                 # better prime checker code
    if n == 1: return False                                                     # sqrt bit doesn't get 1 or 2 right
    if n == 2: return True
    if n % 2 == 0: return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0: return False
    return True


def euler10():
    sum_of_primes = 0
    X = 0

    while X < 2000000:
        if is_prime(X):
            sum_of_primes += X
        X += 1
    return sum_of_primes

#print (euler10())
# 142913828922