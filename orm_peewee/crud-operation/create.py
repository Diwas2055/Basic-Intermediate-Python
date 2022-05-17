# Sample data to insert into the database
def customers():
    return (
        {
            'name': 'John Doe',
            'address': '123 Main Street',
            'phone': 555,
        },
        {
            'name': 'Jane Doe',
            'address': '456 Second Street',
            'phone': 555,
        },
        {
            'name': 'John Smith',
            'address': '789 Third Street',
            'phone': 555,
        },
        {
            'name': 'Jane Smith',
            'address': '654 Fourth Street',
            'phone': 555,
        },
    )


customers()
