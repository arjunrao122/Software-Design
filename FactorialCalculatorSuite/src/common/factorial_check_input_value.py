def check_input_and_run(func):
    def value_check(number):
        if number < 0:
            raise ValueError("Number should be Zero or greater")

        return func(number)

    return value_check
