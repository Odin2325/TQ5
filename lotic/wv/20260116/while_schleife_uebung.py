print('Wähle deinen Kämpfer')
print('Ryu')
print('Ken')
print('Mr. Bison')

while True:
    eingabe = input('Wähle deinen Kämpfer: ')
    if eingabe == 'Ryu':
        print('Du hast Ryu gewählt')
    elif eingabe == 'Ken':
        print('Du hast Ken gewählt')
    elif eingabe == 'Mr. Bison':
        print('Du hast Mr. Bison gewählt')
    nochmal = input('Möchtest du nochmal spielen (y)')
    if nochmal != 'y':
        break

    



'''
user_input = input('Bitte gib eine Zahl ein: ')

while True:
    user_input = input('Bitte gib etwas ein: ')
    print(f'Deine Eingabe war: {user_input}')


while user_input != 'quit': # Geht nur in die Schleife wenn die Eingabe nicht quit ist
    print(f'Deine Eingabe war: {user_input}')
    if user_input != 'quit': 
        break
'''
