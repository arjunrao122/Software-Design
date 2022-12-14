from itertools import count, islice


def compute_prime_number(number):
    return sorted(
                list(islice((numbers for numbers in count(2)
                     if all(numbers % value for value in range(2, numbers))), 0, number)))
