# Importing the Validator class from the cerberus module.
from cerberus import Validator, errors

#! The Cerberus module in python provides powerful yet lightweight data validation functions.
#! It is designed in such a way that you can extend it to various applications and custom validations.

# Validating data present in a dictionary
def example_1():
    schema = {
        'numbers': {'type': 'integer'}
        }
    # Creating a validator object.
    v = Validator(schema)
    data = {'numbers': 5}
    if v.validate(data):
        print("Data is valid")
    else:
        print("Data is invalid")
# Validating with various rules and printing errors
def example_2():
    schema = {
        'id': {'required': True, 'type': 'number'},
        'age': {'type': 'integer'}
        }
    v = Validator(schema)
    if v.validate({'age': 60}):
        print('Data is valid')
    else:
        print('Data is invalid')
        print(v.errors)
        
# Validating with minimum and maximum value ranges
def example_3():
    schema = {
        'name': { 'type': 'string', 'minlength': 5},
        'age': {'type': 'integer', 'min': 18, 'max': 65}
        }
    v = Validator(schema)
    if v.validate({'name': 'VJ', 'age': 16}):
        print('Data is valid')
    else:
        print('Data is invalid')
        print(v.errors)     
        
# Validating with regular expressions
def example_4():
#? Type 1:- 
    schema = {
        'name': {'type': 'string', 'regex': '^[a-zA-Z0-9_]*$'}
        }
    v = Validator(schema)
    if v.validate({'name': 'VJ'}):
        print('Data is valid')
    else:
        print('Data is invalid')
        print(v.errors)  
        
#? Type 2:-
    v = Validator()
    v.schema = {
        "contact_details": {
        "type": "dict",
        "schema": {
            "phone": {
                "type": "string",
                "minlength": 10,
                "maxlength": 10,
                "regex": "^0[0-9]{9}$"
            },
            "email": {
                "type": "string",
                "minlength": 8,
                "maxlength": 255,
                "required": True,
                "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
            }
        }
    }}

    if v.validate(
        {'contact_details': {
            'phone': '0901123123',
            'email': 'john.doe@example.com'
            }
        }):
         print('Data is valid')
    else:
        print('Data is invalid')
        print(v.errors)              

# Validating with custom validator
def custom_validator():
    class CustomValidator(Validator):
        def _validate_type_number(self, field, value):
            if not isinstance(value, int):
                self._error(field, errors.BAD_TYPE)
    schema = {'number': {'type': 'number'}}
    v = CustomValidator(schema)
    if v.validate({'number': "hello"}):
        print('Data is valid')
    else:
        print('Data is invalid')
        print(v.errors)
        
# custom_validator()       
   
# Cerberus custom error messages
def custom_validator_error():
    
    # It's a class that inherits from the BasicErrorHandler class, and it overrides the messages
    # attribute of the BasicErrorHandler class
    class CustomErrorHandler(errors.BasicErrorHandler):
       messages = errors.BasicErrorHandler.messages.copy()
       messages[errors.FORBIDDEN_VALUE.code] = 'Forbidden Value!'
    
    schema = {'animal': {'forbidden': ['Pig']}}
    validator = Validator(schema, error_handler=CustomErrorHandler)
    validator({'animal': 'Pig'})    
    if validator({'animal': 'Pig'}):
        print('Data is valid')
    else:
        print('Data is invalid')
        print(validator.errors)
        
custom_validator_error()    


