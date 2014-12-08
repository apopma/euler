from pip.backwardcompat import raw_input

__author__ = 'Boing'
from os.path import exists

# Calculates all prime numbers up to a given number.

limit = int(raw_input("Check primes up to which number? "))
numbers = [n for n in range(2, limit+1)] # add every testable number to the list Numbers
                                                         # 1 is not prime, needs to be removed manually

primes = [] # define primes (empty for now)

def sieve():
        primes.append(numbers.pop(0)) # pops off the first element in Numbers, adds to Primes (as it is not divisible by any prime found yet))
        n = 0 # iterator
        while n < len(numbers): # while the iterator variable is less than the total length of the list...
                if numbers[n] % primes[-1] == 0: # if the Nth member of Numbers is divisible by the last prime found...
                        del numbers[n] # delete it ( it is not prime )
                else:
                        n += 1

sieve() # need to add an element to primes before starting loop
while primes[-1]**2 < limit:    # until the square of the last prime exceeds the boundary conditions,
        sieve()                                         # keep sieving.
primes += numbers # all leftover numbers are prime

def finalprompt():
        choice = raw_input("""1) print to console\n2) write to file\n\n> """)
        if choice == "1":
                print (str(primes).strip('[]'))
        elif choice == "2":
                filename = raw_input("Enter filename: ")
                def writelist():
                        output = open(filename, 'w')
                        output.write(str(primes).strip('[]'))
                        print ("Finished writing to %s." % filename)
                if exists(filename):
                        if raw_input("Warning! File already exists. Overwrite y/n? ") == "y":
                                writelist()
                        else:
                                finalprompt()

        else:
                print ('Error, please enter "1" or "2"')
                finalprompt()

finalprompt()
print ('=================================================')