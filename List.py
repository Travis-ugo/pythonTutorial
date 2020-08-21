#LIST
numbers = [10, 3, 5 , 2 ,9]
max = numbers[0]
for number in numbers : 
    if number > max :
        max = numbers
print(max)

# 2 DIMENTIONAL LIST
# two dmentional list is a list where every item inside is also a list
# EX
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print (matrix [0][2])

for row in matrix :
    for item in row :
        print(item) 


#TUPLES
# tuples are like lists but tuples cannot be updated or modified 
# ...count(self, x)
# index (self , x, start , end)

 
#UNPACKING :
coordinate = [1 , 2, 3]
x , y , z = coordinate
print(y)

#DICTIONARIES

customer = {
    'name' : 'travis',
    'age' : '11',
    'is_valid' : True
}
customer['karl'] = 'big smoke'
print(customer['karl'])

#EX 
phone = input('phone :')
digits = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four'
} 
output = ''
for love in phone :
    output += digits.get(love , '!') + ' '
print(output)

# Emoji converter 

message = input(' >')
words = message.split(' ')
emojis = {
    ':)' : 'love',
    ':(' : 'sad'
}
output = ''
for word in words :
    output += emojis.get(word, word) + ' '
print(output)    
