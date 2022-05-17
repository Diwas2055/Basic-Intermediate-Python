from pprint import pprint

# import from orm_peewee folder(schema.py) using relative path in __init__.py
import orm_peewee as schema
from create import customers

# Insert data into the database using loop
for customer in customers():
    
    #Exception handling
    try:
        # " **customer " means take all additional named arguments to this function and 
        # insert them into this parameter as dictionary entries.
        schema.Customer.create(**customer)
    except Exception as e:
        print(e)
        exit()
        
pprint('Successfully Created')