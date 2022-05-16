# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    def check():
        num = int(input("Enter a number: "))
        
        # if condition returns True, then nothing happens:
        # if condition returns False, AssertionError is raised:
        assert num % 2 == 0
        if num > 0:
            reciprocal = 1/num
            print(reciprocal)
        else:
            print("Number Must Be Greater than Zero")
    check()
except AssertionError:
    print("Not an even number! Try Again")
    check()
