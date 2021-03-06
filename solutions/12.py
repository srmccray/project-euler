"""
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five hundred divisors.
"""


def get_triangle_number():
    idx = 1
    triangle = 0
    while 1:
        triangle += idx
        yield triangle
        idx += 1


def get_divisors(number):
    div = 0
    for x in range(1, int(number**.5)):
        if not number % x:
            div += 2
    if int(number**.5) * int(number**.5) == number:
        div -= 1
    return div


def get_divisible_triangle_number(divisors=5):
    for x in get_triangle_number():
        if get_divisors(x) > divisors:
            return x


if __name__ == "__main__":
    print(get_divisible_triangle_number(500))
