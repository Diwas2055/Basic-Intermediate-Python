def func2(num1: int, num2: int) -> str:   
    """
    This function takes two integers as input and returns a string.
    
    :param num1: int - This is the first parameter. It's a positional parameter. The name of the
    parameter is num1. The type of this parameter is int
    :type num1: int
    :param num2: int - This is the second parameter, and it's a number
    :type num2: int
    """
    return num1 + num2

# It's calling the function func2 and passing 10 and 20 as arguments.
print(func2(10, 20))
# It's printing the annotations of the function.
print(func2.__annotations__)
# It's printing the docstring of the function.
print(func2.__doc__)


