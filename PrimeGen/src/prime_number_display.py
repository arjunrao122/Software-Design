from prime_number_generator import *


def run_prime_number_display():
    input_number = int(input("Please enter a number greater than or equal to 1: "))
    print("Here are " + str(input_number) + " primes starting from 2: " + ", ".join([str(i) for i in generate_prime_numbers(input_number)]))


if __name__ == '__main__':
    run_prime_number_display()