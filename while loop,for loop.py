call = 0

while call < 3:
    name = input('User name :') 
    call += 1
    if name == 'Travis':
        print('Hey ' + name)
        break
    else:
        print('try again')    
        

for cap in range(3):
    other = input('Other name :')
    if other == 'Okonicha':
        print('Hello ' + name + ' ' + other)
        break
    else :
        print('try again')  

for love in range(3):
    try:
        password = str(int(input('pass word :')))
        if password == str(int('4422')):
            print('Here you Go Boss')
            break
        else:
            print('fake')
    except ValueError :
        print('wrong password')
        