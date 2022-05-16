# Python file one module

import file_two

print("File one __name__ is set to: {}" .format(__name__))

# If this file is being imported from another module, 
# __name__ will be set to the module’s name.
# __name__ is a built-in variable which evaluates to the name of the current module. 
#__main__ is the name of the environment where top-level code is run.

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")