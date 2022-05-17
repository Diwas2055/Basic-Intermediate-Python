# Python Closures are these inner functions that are enclosed within the outer function. 
# Closures can access variables present in the outer function scope. 
# It can access these variables even after the outer function has completed its execution.

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


another = print_msg("Hello")
another()
