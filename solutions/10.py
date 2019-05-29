"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


# naive
# def remove(numbers, prime):
#     return [x for x in numbers if x % prime]
#
#
# def sum_primes(limit=10):
#     primes = []
#     numbers = [x for x in range(2, limit + 1)]
#     count = 0
#     while numbers:
#         count += 1
#         primes.append(numbers[0])
#         numbers = remove(numbers, numbers[0])
#     return sum(primes)


def is_prime(number):
    for x in range(2, int(number**.5) + 1):
        if not number % x:
            return False
    return True


def sum_primes(limit=10):
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total


if __name__ == '__main__':
    print(sum_primes(2000000))
