# Inheritance allows us to define a class that inherits all the methods and 
# properties from another class.
# The parent class is the class being inherited from also called the base class
# The child class is the class that inherits from another class, also called 
# derived class


class Mammal :
    def walk(self):
        print ('dog walkk')
    def Karl(self):
        print('danaa')

class Dog(Mammal) :   # the dog function inherits all the attribute from it parent class "Mammal" as well as the cat function 
    def call(self) :
        print('dog bark')

class cat(Mammal) :
    def catty(self) :        
        print('callable meow')


van = cat()
van.catty()
van.Karl()