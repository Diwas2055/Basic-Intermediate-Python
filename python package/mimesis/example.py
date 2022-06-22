import json

from mimesis import Address
from mimesis.builtins import USASpecProvider
from mimesis.schema import Field, Schema


def user_description():
    f = Field('en', providers=[USASpecProvider])
    a = Address('en')
    return {
        'id': f('uuid'),
        'name': f('full_name'),
        'email': f('person.email'),
        'timestamp': f('timestamp', posix=False),
        'car_model': f('car'),
        'address': {
            'full_address': f('address'),
            'city': f('city'),
            'zip_code': f('zip_code')
        }
    }


schema = Schema(schema=user_description)
data = schema.create(iterations=2)

with open("user.json", "w") as fixture:
    json.dump(data, fixture)