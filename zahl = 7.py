'''
zahl = 7

if zahl > 5:
    print('größer als 5')
elif zahl > 0:
    print('positiv')
'''
'''
zahl = 3

if zahl > 5:
    print('A')
elif zahl > 2:
    print('B')
elif zahl > 0:
    print('C')
else:
    print('D')
'''
'''
zahl = int(input('Gib eine Zahl ein: '))

if zahl < 0:
    print('negativ')
elif zahl == 0:
    print('null')
elif zahl < 10:
    print('kleine positiv')
else:
    print('groß positiv')
'''
'''
alter = 18

if alter < 12:
    print('Du bist ein Kind.')
elif alter <= 17:
    print('Du bist ein Teenager.')
else:
    print('Du bist erwachsen.')
'''

'''
for zahlen in range(1, 6):
    print(zahlen)
'''
'''
counter = 3

while counter > 0:
    print(counter)
    counter = counter -1    # man kann auch so schreiben counter -= 1 oder counter += 1 wenn man dazu zählen will

print('Abflug')
'''
'''
for zahl in range(1,11):
    if zahl == 7:
        print('Gefunden')
    else:
        print(zahl)
'''
'''
# Aufgabe A:

geld = 40

if geld > 100:
    print('Du bist reich!')
elif geld >= 50:
    print('Das reicht für das Ticket.')
else:
    print('Zu wenig Geld')
'''
'''
# Aufgabe B:

for zahl in range(5, 0, -1):
    print(zahl)
'''
'''
# Aufgabe C:

passwort = ''

while passwort != 'geheim':
    passwort = input('Bitte Passwort eingeben: ')

print('Zugriff erlaubt')
'''
'''
geld = 0

while geld < 50:
    geld = int(input('Wieviel Geld werfen Sie ein? '))
    
    if geld < 50:
        print('Nicht genug! Bitte mehr einwerfen')

print('Ticket wird gedruckt')
'''
'''
tipp = 0

while tipp != 7:
    tipp = int(input('Rate die Zahl (1-10): '))
    
    if tipp < 7:
        print('Zu niedrig!')
    elif tipp > 7:
        print('Zu hoch!')

print('Richtig geraten!')
'''
'''
zahlenliste = [15, 2, 39, 72, 142]
zahlenliste2 = []

for zahl in range(0, 5):

    # zahlenliste[zahl] *= 2 # Verdoppelt jedes zahl aus der liste!
    zahlenliste2.append(zahlenliste[zahl] * 2) # fügt die gesamte erste liste in eine 2 liste (kopie) und verdoppelt jedes elemente der liste

print(zahlenliste)

print(zahlenliste2)

zahlenliste.pop(3)  # Element aus der Liste Löschen (index 3 also das 4 element aus der liste)
print(zahlenliste)
'''

zahlenliste = [15, 2, 39, 72, 142]

zahlenliste2 = []
zähler = 0
listenlänge = len(zahlenliste)      #mit deise variabloe zählt er die liste nur einmal also die länge der liste, dadurch spart er zeit!

while zähler < listenlänge:
   # print(zähler)       # fängt ab 0 an zu zählen da die 0 nach erste ausgabe addiert wier.
    # zahlenliste[zähler] = zahlenliste[zähler] * 2
    zahlenliste2.append(zahlenliste[zähler] * 2)
    zähler += 1         # print(zähler)     # fängt ab 1 an zu zählen da die 1 schon vor der ausgabe addiert wird.



print('Liste 1')
print(zahlenliste)

print('Liste 2')
print(zahlenliste2)

'''
import random

tipp = random.randint(1, 100)
eingabe = 0
versuchtespiele = 0

while tipp != eingabe:
    eingabe = int(input('Rate die Zahl (1-100): '))
    
    versuchtespiele += 1

    if eingabe < tipp:
        print('Zu niedrig!')
    elif eingabe > tipp:
        print('Zu hoch!')
    if versuchtespiele >= 10:
        break

if tipp == eingabe:
    print(f'Richtig geraten nach {versuchtespiele} versuche Spiele!')
else:
     print('Maximale versucher erreicht! GAME OVER!')
'''

'''
import random

liste = []

for zähler in range(0, 10):
    zufallszahl = random.randint(1, 20)
    liste.append(zufallszahl)
    
    
print(liste)
'''


'''
import random

def ratespiel():
    zufallszahl = random.randint(1, 100)
    geraten = 0
    leben = 10
    versuche = 0

    while zufallszahl != geraten:
        print(f'Du hast noch {leben-versuche} Leben übrig')
        geraten = int(input('Bitte gib eine Zahl von 1-100 ein: '))
        versuche += 1
        if geraten < zufallszahl:
            print('Deine Zahl ist zu klein')
        if geraten > zufallszahl:
            print('Deine Zahl ist zu groß')
    print(f'Richtig geraten! Du hast {versuche} Versuche gebraucht und noch {leben-versuche} Leben übrig.')


while True:
    ratespiel()
    nochmal = input('Möchtest du nochmal spielen? (y)')
    if nochmal != 'y':
        break
'''