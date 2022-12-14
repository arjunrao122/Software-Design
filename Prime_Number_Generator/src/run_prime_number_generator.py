from src.compute_prime_numbers import *   # pragma: no cover
from src.get_user_input import *    # pragma: no cover


def main():    # pragma: no cover
    input_number = int(input("Please enter a number greater than or equal to 1: "))
    number = get_user_input(input_number)
    print("Here are " + str(number) + " primes starting from 2: " + ", ".join([str(i) for i in compute_prime_number(number)]))

