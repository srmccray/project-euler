"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def is_prime(num, primes):
    for x in primes:
        if not num % x:
            return False
    return True


def find_prime(num=6):
    primes = []
    x = 1
    while len(primes) < num:
        x += 1
        if is_prime(x, primes):
            primes.append(x)
    return x


# # naive solution, 104743
# def is_prime(num):
#     for x in range(2, num):
#         if not num % x:
#             return False
#     return True
#
#
# def find_prime(num=6):
#     prime_count = 0
#     idx = 1
#     while prime_count < num:
#         idx += 1
#         if is_prime(idx):
#             prime_count += 1
#     return idx


if __name__ == "__main__":
    print(find_prime(10001))
    # print(find_prime(10001))
