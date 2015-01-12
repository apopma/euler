import concurrent.futures
import math

__author__ = 'apothem'

""" Project Euler problem #3: prime factors
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
"""

''' Pseudocode:
Accept a target to find the biggest prime factor of
Generate a list of all prime numbers, from the biggest prime <= target, to 2

Test each prime from biggest to smallest, to see if it's a factor of target
The first prime that IS a factor of the target is the biggest prime factor! Return it.
'''

global_target = 600851475143                                                    # ugly but it works

def is_prime(n):                                                                # better prime checker code
    if n % 2 == 0:                                                              # doesn't mark 2 as prime,
        return False                                                            # but for this application it's OK

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def make_primes(target, span):
    print ("Running prime maker...\n")
    PRIMES = [x for x in range(target, (target - span), -1)]                    # still a bad idea

    primeslist = open('primes.txt', 'w')
    with concurrent.futures.ProcessPoolExecutor() as executor:                  # black sorcery from the Python docs
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):       # breaks if it isn't executed using
            if prime:                                                           # if __name__ == '__main__':
                primeslist.write(str(number) + "\n")
                #print ("Found prime: {}".format(number))
    primeslist.close()
    print ("Made primes.")


def find_bpf(target, span):
    found_bpf = False

    print ("Finding biggest prime factor of {:d} with span {:d}...".format(target, span))
    make_primes(target=target, span=span)
    print ("Running factor tests...")

    with open('primes.txt', 'r') as infile:
        for line in infile.readlines():
            candidate = int(line)
            if global_target % candidate == 0:
                print ("Found the biggest prime factor: {:d}!".format(candidate))
                found_bpf = True
                return found_bpf
        if not found_bpf:
            print ("Couldn't find the biggest prime factor. :(\n")
            found_bpf = False
            return found_bpf


if __name__ == '__main__':
    target = math.floor(global_target / 2)
    span = 100000
    new_target = target
    count = 0
    print ("Biggest Prime Factor Finder 9000:")

    done = find_bpf(target=global_target, span=span)
    count += 1
    while not done:
        new_target = (new_target - span)
        print ("Searching again with new target {:d} and span {:d}.".format(new_target, span))
        print ("Searched {:d} times so far, for numbers from {:d} to {:d}.".format(count, global_target, (global_target - target - (count * span))))
        done = find_bpf(target=new_target, span=span)
        count += 1