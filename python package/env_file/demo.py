import os
from pprint import pprint

from dotenv import load_dotenv, find_dotenv,dotenv_values

# Loading the environment variables from the .env file.
load_dotenv()

pprint(dotenv_values(".env"))

# The above code is printing the value of the environment variable DOMAIN.
print('Domain :- ' +" " + os.getenv('DOMAIN'))