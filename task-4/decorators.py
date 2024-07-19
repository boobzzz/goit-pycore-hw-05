from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args):
        result = None
        try:
            result = func(*args)
        except Exception as e:
            print(f"{type(e)}: {e}")

        return result

    return inner
