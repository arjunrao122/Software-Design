from functools import wraps


def character_blocker(func):
    @wraps(func)  # This copies metadata from func to the wrapper function
    def blocker(text):
        return text.replace(func(text), "")
    return blocker
