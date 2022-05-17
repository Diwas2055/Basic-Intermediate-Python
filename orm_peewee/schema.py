from peewee import *

# Connection to database
db = PostgresqlDatabase('test_orm', host='localhost',
                        port=5432, user='postgres', password='root')


# Connect to database , give result in boolean format
# db.connect()

# Create Model class

# BaseModel Created To Provide The Base Class For All Models
class BaseModel(Model):
    class Meta:
        database = db


# Customer Model Created

class Customer(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    address = TextField()
    phone = IntegerField()

    class Meta:
        db_table = 'customer'


# Invoice Model Created


class Invoice(BaseModel):
    id = IntegerField(primary_key=True)
    invoice_no = IntegerField()
    amount = IntegerField()

    class Meta:
        db_table = 'Invoices'


# Check if database is connected
if db.connect():
        
    # The create_table() method is a classmethod of Model class that performs equivalent CREATE TABLE query.
    db.create_tables([Customer])
    print("Table created")

    # Multiple tables can be created using this method.
    # db.create_tables([Customer, Invoice])
    # print("Multiple tables created")
else:
    print('Error connecting to database')
    exit()
