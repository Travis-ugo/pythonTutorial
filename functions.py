# def : short form of define, it is used to define a function 

def kandy_user() :
    print('hey there')
    print('welcome')

print('start')
kandy_user()
print('distinguish')    

#parameter
# A parameter s a placeholder for recieving information
# Argument : the actual piece of information that is supplied to a function

# def kandy_user(name) :
#   print(f'hi {name}')
#  print('welcome') 

# key word Arguments
     # having the parameter name followed by the parameter
     # with keyword arguments the position doesnt really matter
     

# EXCEPTIONS :

try :
    age = int(input('input age : '))
    print(age)
except ValueError :
    print('invaid error')     

try : 
    age = int(input('age : '))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError :
    print('invalid')
except ValueError :
    print('inavlid number')

# Try except blocks are used to handle exceptions raised in our program 
# and make sure the program doesnt crash 

# NOTE :
#        many exceptions can be used .

 
# COMMENTS :
#            comments are statements writen to guide the programmer or
#            remind . comments are not executed by the computer system
#            use (#) to write a comment           
