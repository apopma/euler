__author__ = 'Adam'


""" Project Euler problem #3: prime factors
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
"""

''' Pseudocode:
Accept a target to find the biggest prime factor of
Generate a list of all prime numbers, from the biggest prime <= target, to 2

Test each prime from biggest to smallest, to see if it's a factor of target
The first prime that IS a factor of the target is the biggest prime factor! Return it.

Way to do it with less memory:
    Manually add 2 to primes, never generate any multiples of 2
    Only generate 200,000 or so entries of 'numbers' at any one time
    Sieve those entries, add the sieved entries to a lookup table
    Continue generating the entries and sieving until the entire list has been sieved

    Add the first member of the sieved lookup table to primes; it is prime
    Sieve the lookup table again, 200,000 or so at a time
    Lather, rinse, repeat
'''

class Memoize(object):          # ?????????????
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

class Euler3(object):
    def __init__(self, target):
        self.target = int(target)
        self.numbers = [x for x in range(2, self.target + 1)]       #this is a very bad idea
        self.primes = []

    def sieve(self):
        self.primes.append(self.numbers.pop(0))
        n = 0

        while n < len(self.numbers):
            if self.numbers[n] % self.primes[-1] == 0:
                del self.numbers[n]
            else:
                n += 1

    def make_primes(self):
        print ("Running prime maker...")
        Euler3.sieve(self)
        while self.primes[-1] ** 2 < self.target:
            Euler3.sieve(self)
        self.primes += self.numbers

    def biggest_prime_factor(self):
        Euler3.make_primes(self)
        print ("Made primes.")

        sorted_primes = sorted(self.primes, reverse=True)
        print (sorted_primes)
        biggest_prime = int(sorted_primes.pop(0))
        print ("Running factor checking...")

        while len(sorted_primes) > 0:
            if self.target % biggest_prime == 0:
                print ("Found biggest factor!")
                return biggest_prime
            elif self.target % biggest_prime != 0:
                biggest_prime = sorted_primes.pop(0)


euler3 = Euler3(600851475143)
euler3.biggest_prime_factor()