from faker import Faker
import random
import json

class LoginData:

    def __init__(self):
        fake = Faker()
        self.password = "password@123"
        self.email = fake.email()
        self.username = fake.first_name()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.phone = random.randint(9000000000, 9999999999)
        self.city = fake.city()
        self.about = "This is a sample text : about"

    def get_json(self):
        p = {
            'password': self.password,
            'email': self.email,
            'username': self.first_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'city': self.city,
            'about': self.about
        }
        return p



def input_data(x):
    data = []
    for i in range(0, x):
        login_data = LoginData()        
        # print(login_data.get_json())
        datum = login_data.get_json()
        data.append(datum)
    return data


def main():
    no_of_input = 1000
    data = input_data(no_of_input)
    with open('python package/faker/customer.json', 'w', encoding='utf-8') as f:
     json.dump(data, f, ensure_ascii=False, indent=4)
    print("File has been created.")


main()