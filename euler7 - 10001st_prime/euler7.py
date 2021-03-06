__author__ = 'apothem'
import math

'''
Project Euler problem #7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13; we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def is_prime(n):                                # better prime checker code w/bits for 1 and 2
    import math
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0: return False
    return True


def euler7():
    current_prime = 0
    this = 0
    prime_index = 0
    target = 10001

    while prime_index < target:
        if is_prime(this) is True:
            current_prime = this
            prime_index += 1
 #           print ("Prime #{} is {}".format(prime_index, current_prime))
        if prime_index == target:
            print ("Found target #{}".format(prime_index))
            break
        this += 1

    return current_prime

print (euler7())