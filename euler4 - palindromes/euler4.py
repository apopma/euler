__author__ = 'apothem'
import math

'''
Project Euler problem #4: palindromic numbers

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

                                Answer is not 580085
'''

# len() gives you the value of the last index +1
# foo[-len(foo)] is foo[0], can't go smaller

product_list = []


def make_product_list(number1, number2, lower_limit):

    while number2 > lower_limit:
        product_list.append(str(number1 * number2))             # duck typing to allow iteration
        number2 -= 1
#    print (product_list)


def check_palindrome(candidate):
    x = 0
    y = -1

    for foo in range (0, math.floor(len(candidate) / 2), 1):      # only checks first half, ignores middle index if odd
        if candidate[x] != candidate[y]:
#            print ("Digit pair {} / {} did not match in candidate {}".format(candidate[x], candidate[y], candidate))
            return False
        x += 1
        y -= 1
    print ("Found a palindrome in candidate {}".format(candidate))
    return True


def euler4():
    m = 999
    n = 999
    biggest_palindrome = 0

    found_palindrome = False
    print ("Palindrome Finder 9001:")

    make_product_list(number1=m, number2=n, lower_limit=99)
    for i in range (0, len(product_list), 1):
        found_palindrome = check_palindrome(candidate=product_list[i])

    while m >= 100:
        print ("Checking palindromes for {} and {}.".format(m, n))

        n -= 1
        if n <= 99:
            m -= 1
            n = m - 1

        product_list.clear()
        make_product_list(number1=m, number2=n, lower_limit=99)

        for i in range (0, len(product_list), 1):
            found_palindrome = check_palindrome(candidate=product_list[i])
            if found_palindrome is True:
                if int(product_list[i]) > biggest_palindrome:
                    biggest_palindrome = int(product_list[i])

    return biggest_palindrome

print (euler4())