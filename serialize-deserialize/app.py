""" Serialization is a process in which an object is 
 transformed into a format that can be stored/save (in a file or memory buffer) """

# todo:- There are two basic formats for JSON data.
# todo:- Either in a string or the object datastructures.
# todo:- The object datastructures, in Python, consists of lists and dictionaries nested inside each other.
# todo:- The object datastructures allows one to use python methods (for lists and dictionaries) to add,
# todo:- list, search and remove elements from the datastructures.
# todo:- The String format is mainly used to pass the data into another program
# todo:- or load into a datastructures.

import pickle
import json
from pprint import pprint

""" Json.loads """

# !To load JSON back to a data structure, use the "loads" method.
# !This method takes a string and turns it back into the json object datastructures:

json_string = """{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""
print(json.loads(json_string))


""" Json.dumps """
# !json.dumps() function converts a Python object into a json string.

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)


""" Pickle """

# ?The pickle module is used for implementing binary protocols for
# ?serializing and de-serializing a Python object structure.

""" Serialize """
# todo:- dumps() – This function is called to serialize an object hierarchy.

friend1 = {"Dan": [20, "London", 3234], "Maria": [22, "Paris", 7876]}
friend2 = {"Joey": [23, "New-york", 32394], "Ross": [25, "Washington", 786776]}
friends = (friend1, friend2)
# !wb:- write in binary mode
with open('friends.txt', 'wb') as f:
    # pickle.dump(data,file)
    pickle.dump(friends, f)


""" Deserialize """
# todo:- loads() – This function is called to de-serialize a data stream.
# !rb:- read in binary mode
with open('friends.txt', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    pprint(obj)
