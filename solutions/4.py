"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(num):
    chars = str(num)
    for idx in range(int(len(chars)/2)):
        if chars[idx] != chars[-1 - idx]:
            return False
    return True


def largest_palindrome_product():
    for x in range(999999, 100000, -1):
        if is_palindrome(x):
            for y in range(999, 100, -1):
                if not x % y and 99 < x/y < 1000:
                    return x


if __name__ == '__main__':
    print(largest_palindrome_product())
