from operator import mul
from functools import reduce
from src.factorial_imperative_iteration import check_input_and_run


@check_input_and_run
def factorial(number):
    return reduce(mul, range(1, number + 1), 1)
