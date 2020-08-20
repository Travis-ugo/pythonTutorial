print('Guess game')
secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess = int(input('Guess : '))
    guess_count += 1
    if guess == secret_number :
        print('you win')
        break
else :
    print('you loss')

print ('Car game')
command = ''
 # while command != 'quit' :       both of them works
while True :
    command = input('>>').lower()
    if command == "start" :
        print('car started')
    elif command == 'stop' :
        print('car has stopped')
    elif command == 'help' :
        print('''
start - to start the car
stop - to stop the car
quit - to quit game
        ''')
    elif command == 'quit' :
        print('game ended')
        break
    else : 
        print('try again')