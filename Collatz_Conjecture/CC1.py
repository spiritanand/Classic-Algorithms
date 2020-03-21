"""
Collatz Conjecture - Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""


def cc1():
    counter = 0
    n = int(input("Enter the number(>1) which has to be checked :- "))
    if n < 1:
        raise ValueError("The number entered must be greater than +1")
    while n > 1:
        if n % 2 == 0:
            n = n/2
            counter += 1
        else:
            n = (n*3) + 1
            counter += 1
    print("Therefore, the number of steps to reach 'one' is :- ", counter)
