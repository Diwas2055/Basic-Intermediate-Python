# Iterables: An object capable of returning its member one at a time is called an iter-able.
# An iterator is an object, which is used to iterate over an iterable object using the __next__() method.

#  Example 1: Iterating over a list

def simple_iter():
    iterable = [1, 2, 3, 4]
    iter_obj=iter(iterable)

    while True:
        try:
            print(next(iter_obj))
        except StopIteration:
            break

# Example 2: Generator function that yields one item at a time        
class PowersOfTwo:

   def __iter__(self):
       self.num = 2
       return self

   def __next__(self):
       ans = self.num
       self.num *= 2
       return ans

two_powers = PowersOfTwo()
iter_obj = iter(two_powers)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))       

# Example 3: Iterator to print English alphabets from A to Z

class Alphabets:
   def __iter__(self):
       self.unicode = 65
       return self
   def __next__(self):
       if self.unicode > 90:
           raise StopIteration
       temp = self.unicode
       self.unicode += 1
       return chr(temp)
alphabets = Alphabets()
iter_obj = iter(alphabets)
for letter in iter_obj:
   print(letter, end=" ")