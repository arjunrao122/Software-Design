from src.common.factorial_check_input_value import check_input_and_run


@check_input_and_run
def factorial(number):
    return 1 if number == 0 else number * factorial(number - 1)
