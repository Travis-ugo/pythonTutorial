# A Class in python is like an object constuctor or a blueprint for creating object.
# all classes have function called __init__(), which always executes when the class 
# is being initiated.
# use the __init__() function to assign values to object properties, or other operationns
# that are nessesary to do when th object is created

class Person :
    def __init__(self, name , age , year) :
        self.name = name
        self.age = age
        self.year = year

    def Fun(self) :
        print('cally got them boys' + self.name + str(int( self.age)) )

clout = Person(' nana', 27 , 1999) 
clout.Fun()

# NOTE: The self parameter is a reference to the current instance of the class,
#       and is used to access variablles that belongs to the class .
#       it doesnt have to be named "SELF"