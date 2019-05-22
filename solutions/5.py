"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from functools import reduce


def can_be_divided(num):
    for x in range(1, 20):
        if num % x:
            return False
    return True


def is_prime(num):
    for x in range(2, num):
        if not num % x:
            return False
    return True


def smallest_multiple(num=0):
    multiple = []
    for x in range(2, num + 1):
        if is_prime(x):
            multiple.append(x)
        else:
            for y in multiple:
                if (x**(1/y)).is_integer():
                    if multiple.count(y) < (x**(1/y)):
                        multiple.append(y)
    return reduce((lambda a, b: a * b), multiple)

# naive solution
# def smallest_multiple():
#     x = 0
#     while 1:
#         x += 20
#         if can_be_divided(x):
#             return x


if __name__ == "__main__":
    print(smallest_multiple(20))
