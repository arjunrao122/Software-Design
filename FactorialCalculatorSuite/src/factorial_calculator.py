# factorial_calculator.py
from factorial_functional_iterator import factorial as factorial_functional
from factorial_imperative_iteration import factorial as factorial_imperative
from factorial_simple_recursion import factorial as factorial_recursive


def run_factorial_calculator():
    print("Factorial Calculator")
    print("1: Functional Iterator Method")
    print("2: Imperative Iteration Method")
    print("3: Simple Recursion Method")

    choice = input("Choose a method (1-3): ")
    number = int(input("Enter a non-negative integer: "))

    try:
        if choice == '1':
            result = factorial_functional(number)
        elif choice == '2':
            result = factorial_imperative(number)
        elif choice == '3':
            result = factorial_recursive(number)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            return

        print(f"The factorial of {number} is {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    run_factorial_calculator()
