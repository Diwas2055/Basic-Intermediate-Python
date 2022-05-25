import redis

_redis = redis.Redis(host='localhost', port=6379)

#set value in the key value mechanism
_redis.set("TestA", "testA")

#get the value from redis buffer
print("TestA:", _redis.get("TestA"))

#delete the value from buffer
_redis.delete("TestA")
print("TestA", _redis.get("TestA"))



import redis
import json

_redis = redis.Redis(host='localhost', port=6379)

# The Person class is a blueprint for creating objects that have a name and an age.
class Person():
    pass

# Creating a new instance of the Person class and setting the attributes of the instance.
p = Person()
p.Name = "OK"
p.age = 10
p.Bloodgroup = "A+"

# Converting the object to a dictionary and then converting the dictionary to a string.
_redis.set("TestB", json.dumps(p.__dict__))
print(_redis.get("TestB"))