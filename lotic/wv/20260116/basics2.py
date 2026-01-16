name = input('Bitte gebe den Name ein: ')

mein_name = 'Ionut Strainescu'
age = '40'
city = 'Nürnberg'

#is_woman = False # ist_frau = Falsch
is_woman = True # ist_frau = Wahr 

if is_woman:
    print('Sehr geehrte Frau ' + name + ',') # Zeile 11 und 12 geben das gleiche aus.
    print(f'Sehr geehrte Frau {name},')  # f-String Zeile 11 und 12 geben das gleiche aus.
else:
    print('Sehr geehrter Herr ' + name + ',')

print('') # Diese Zeile ist obsolet wenn wir \n in der nächsten Zeile benutzen.
print('\nMein Name ist ' + mein_name + '.') #\n ergibt Zeilenumbruch
print('Ich bin ' + age + ' Jahre alt.')
print('Ich komme aus ' + city + '.')
input('Bitte beliebige Taste drücken...')
