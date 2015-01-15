__author__ = 'apothem'

"""
Project Euler problem #3: prime factors
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
"""


global_target = 600851475143                                                    # ugly but it works

def is_prime(n):
    import math                                                                 # better prime checker code
    if n == 1: return False                                                     # sqrt bit doesn't get 1 or 2 right
    if n == 2: return True
    if n % 2 == 0: return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0: return False
    return True

# 6857
def euler3():
    X = 2
    candidate = 0
    biggest_prime_factor = 0
    prime_factors = []

    while X < global_target:
        if is_prime(X):
            candidate = X
        if global_target % candidate == 0:
            prime_factors.append(int(candidate))
            if candidate > biggest_prime_factor:
                biggest_prime_factor = int(candidate)
                print "Biggest prime factor so far is %s" % biggest_prime_factor
        X += 1

        if X % 10000000 == 0:
            print "Searched up to %s" % X

    return biggest_prime_factor

print euler3()