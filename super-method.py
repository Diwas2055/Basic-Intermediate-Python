
#! super() :- method returns a proxy object that allows us 
#!             to access methods of the base class.

#? Syntax:
# super(type, object)

#? Parameters:
#  a. type: (Optional) The class name whose base class methods needs to be accessed
#  b. object: (Optional) An object of the class or self.


class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
   # Calling the __init__ method of the parent class.
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')