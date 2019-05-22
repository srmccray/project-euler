"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def sum_multiples(x, y, limit):
    multiples = []
    for val in range(0, limit):
        if not val % x or not val % y:
            multiples.append(val)
    return sum(multiples)


if __name__ == '__main__':
    print(sum_multiples(3, 5, 1000))
