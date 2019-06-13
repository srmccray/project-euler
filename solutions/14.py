"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


collatz_sequences = {}


def get_collatz_sequence_length(number=13):
    start = number
    count = 1
    while True:
        if collatz_sequences.get(number):
            collatz_sequences[start] = collatz_sequences.get(number) + count - 1
            return collatz_sequences.get(number) + count - 1
        if number % 2:
            number = 3 * number + 1
        else:
            number = number / 2
        count += 1
        if number == 1:
            collatz_sequences[start] = count
            return count


def get_longest_collatz_sequence(number=13):
    max_length, value = 0, 0
    for x in range(2, number + 1):
        length = get_collatz_sequence_length(x)
        if length > max_length:
            max_length, value = length, x
    return value


# def get_collatz_sequence(number=13):
#     results = [number, ]
#     while True:
#         if number % 2:
#             number = 3 * number + 1
#         else:
#             number = number / 2
#         results.append(int(number))
#         if number == 1:
#             return results
#
# def get_longest_collatz_sequence(number=13):
#     max_length, collatz_number = 0, 0
#     for x in range(2, number + 1):
#         seq = get_collatz_sequence(x)
#         seq_length = len(seq)
#         print(x, seq)
#         if seq_length > max_length:
#             max_length, collatz_number = seq_length, x
#     return collatz_number, max_length


if __name__ == "__main__":
    print(get_longest_collatz_sequence(1000000))
