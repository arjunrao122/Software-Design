from operator import mul
from functools import reduce
from src.common.factorial_check_input_value import check_input_and_run



@check_input_and_run
def factorial(number):
    return reduce(mul, range(1, number + 1), 1)
