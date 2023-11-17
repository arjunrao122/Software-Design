from src.common.factorial_check_input_value import check_input_and_run


@check_input_and_run
def factorial(number):
    product = 1

    for numbers in range(1, number + 1):
        product *= numbers

    return product
