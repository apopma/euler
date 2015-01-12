__author__ = 'apothem'

'''
Project Euler problem #5: remainders
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def check_remainder(candidate):
    for i in range (1, 21, 1):
        if candidate % i != 0:
            return False
    print (candidate)
    return True

def euler5():
    found_answer = False

    X = 1
    found_answer = check_remainder(X)

    while not found_answer:
        X += 1
        print ("Checking {}".format(X))
        found_answer = check_remainder(X)
        if found_answer is True:
            print ("Found it! The answer is {}.".format(X))
            break

# got to 210937438 w/o answer
euler5()
