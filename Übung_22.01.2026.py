#   Aufgabe 1:
# Schreibe ein Programm, das den Nutzer nach seinem Alter fragt.
# Unter 18: "Zutritt verboten."
# 18 bis 66: "Willkommen!"
# Ab 67: "Willkommen, genießen Sie den Ruhestand!"
''' 
alter = int(input('Bitte alter eingeben: '))

if alter < 18:
    print('Zutritt verboten!')
elif alter <= 66:
    print('Willkommen!')
else:
    print('Willkommen, genießen Sie den Ruhestand')
'''

#   Aufgabe 2:
# Erstelle eine for-Schleife, die die 5er-Reihe von 1⋅5 bis 10⋅5 berechnet und ausgibt.
# Ziel-Output: "1 mal 5 ist 5", "2 mal 5 ist 10", etc.
'''
for i in range(1, 11):
    ergebniss = i * 5
    print(f'{i} mal 5 ist {ergebniss}')
'''

#   Aufgabe 3:
# Erstell eine Liste mit 50 Zufallszahlen zwischen 1-100. Gib anschließend für jede Zahl aus, ob sie größer als 50 oder kleiner als 50 war.
import random

zahlen = [1, 100]

for i in range(50):
    neue_zahl = random.randint(1, 100)
    zahlen.append(neue_zahl)

for zahl in zahlen:
    if zahl > 50:
        print(zahl, 'ist größer als 50')
    elif zahl < 50:
        print(zahl, 'ist kleiner als 50')
    else:
        print(zahl, 'ist genau 50')

'''
zahlen = [random.randint(1, 100) for _ in range(50)]

for zahl in zahlen:
    if zahl > 50:
        print(f'{zahl} ist größer als 50')
    elif zahl < 50:
        print(f'{zahl} ist kleiner als 50')
    else:
        print(f'{zahl} ist genau 50')
'''