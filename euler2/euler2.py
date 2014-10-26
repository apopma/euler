# PROJECT EULER PROBLEM 2: EVEN FIBONACCI NUMBERS

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
from pip.backwardcompat import raw_input

fibonacci = [1, 2]


def make_fibonacci(max_fibo):
    for i in range(0, max_fibo, 1):
        new_fibo = fibonacci[i] + fibonacci[i + 1]
        if new_fibo <= max_fibo:
            fibonacci.append(new_fibo)
        else:
            print('Fibonacci maker ended at value %s.' % new_fibo)
            print (fibonacci)
            break


def sum_even_fibo():
    fibo_sum = 0
    for i in range(0, len(fibonacci)):
        if fibonacci[i] % 2 == 0:
            fibo_sum += fibonacci[i]
    print('Sum of even Fibonaccis in this sequence is %s.' % fibo_sum)


max_fibo = int(raw_input('Enter a value to end the Fibonacci sequence at:'))
make_fibonacci(max_fibo)
sum_even_fibo()