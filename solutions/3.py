"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(num, start=1):
    for x in range(start, num):
        if not num % x:
            result = largest_prime_factor(int(num / x), start=x+1)
            return result if result else int(num/x)


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
