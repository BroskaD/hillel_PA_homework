from functools import wraps
from math import ceil


def print_log(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'{function.__name__} была исполнена')
        return function(*args, **kwargs)

    return wrapper


@print_log
def is_simple_number(n):

    '''Return True if n is prime number.'''

    if n <= 1 or isinstance(n, float):
        print('Incorrect input number. Enter positive natural number')
        return None

    # optimized divisor enumeration
    for k in range(2, ceil(n ** 0.5) + 1):
        if n % k == 0 and n != k:
            return False

    return True


print(is_simple_number(10))
print(is_simple_number(5))
print(is_simple_number(17))
print(is_simple_number(9))
