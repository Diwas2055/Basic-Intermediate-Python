# Nested Dictionary
from faker_schema.faker_schema import FakerSchema

schema = {'EmployeeInfo': {'ID': 'uuid4', 'Name': 'name', 'Contact': {'Email': 'email',
          'Phone Number': 'phone_number'}, 'Location': {'Country Code': 'country_code',
          'City': 'city', 'Country': 'country', 'Postal Code': 'postalcode',
          'Address': 'street_address'}}}
faker = FakerSchema()
data = faker.generate_fake(schema)

print(data)

# Generating a certain number of fake data from given schema

from faker_schema.faker_schema import FakerSchema

schema = {'employee_id': 'uuid4', 'employee_name': 'name', 'employee address': 'address',
          'email_address': 'email'}
faker = FakerSchema()
data = faker.generate_fake(schema, iterations=4)
print(data)