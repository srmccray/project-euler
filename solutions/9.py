"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def find_triplet(num=12):
    for a in range(1, num):
        for b in range(a + 1, num):
            x = a**2 + b**2
            c = x**.5
            if c.is_integer():
                if a + b + c == num:
                    return a * b * c


if __name__ == "__main__":
    print(find_triplet(1000))
