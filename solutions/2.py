"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def generate_fibonacci(limit=10):
    fib = 0
    fib_1 = 1
    fib_2 = 2
    yield fib_1
    yield fib_2
    while fib < limit:
        fib = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib
        yield fib


def even_fibonacci(limit=10):
    result = 0
    for num in generate_fibonacci(limit):
        if not num % 2:
            result += num
    return result


if __name__ == '__main__':
    print(even_fibonacci(4000000))
