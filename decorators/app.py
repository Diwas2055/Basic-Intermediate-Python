# Python decorators are pieces of code that allow existing functions to be added to or
# modified when they are run, without modifying the underlying function definition.
# This is known as meta-programming because the program itself attempts to modify
# another part of itself when the program is run.

""" Using Python Decorators to Log Useful Info to the Terminal """

from datetime import datetime
import sys


def log_info(func):
    def inner():
        print(f'Starting run at {datetime.now()}')
        print('Running', func.__name__)
        func()
    return inner


""" without using @log_info: """


def print_welcome():
    print('Welcome to Python World!')


print_welcome = log_info(print_welcome)
print_welcome()


""" with using @log_info: """


@log_info
def print_welcome():
    print('Welcome to Python World!')


print_welcome()


""" Passing Arguments into Python Decorators """

# Special Symbols Used for passing arguments:-

# 1.)*args (Non-Keyword Arguments) example:- (1, 2, 3)

# 2.)**kwargs (Keyword Arguments) example:- {'name': 'John', 'age': '25'}


def print_function_name(func):
    # func_name(*args, **kwargs), which will unpack all arguments and all keyword arguments
    def inner(*args, **kwargs):
        print(f'Running {func.__name__}...')
        return func(*args, **kwargs)
    return inner


@print_function_name
def add_more_nums(a, b, c, d):
    print(a + b + c + d)


add_more_nums(1, 2, 3, 4)
