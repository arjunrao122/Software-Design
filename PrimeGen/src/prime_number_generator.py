from itertools import count, islice


def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))


def generate_prime_numbers(limit):
    return sorted(
                list(islice((numbers for numbers in count(2)
                     if is_prime(numbers)), 0, limit)))
