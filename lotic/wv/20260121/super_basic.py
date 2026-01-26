'''
Aufgabe1:
Gegeben ist folgende Liste: [15, 2, 39, 72, 142]
Schreibe eine App die jede Zahl in der Liste verdoppelt.
'''
'''
print(zahlenliste)
print(zahlenliste[0])
print(zahlenliste[1])
print(zahlenliste[2])
print(zahlenliste[3])
print(zahlenliste[4])
'''

#Start
zahlenliste = [15, 2, 39, 72, 142]
#Ziel
#zahlenliste2 = [30, 4, 78, 144, 284]

zahlenliste2 = []

for zahl in range(0, 5):
    #print(zahl)
    #print(zahlenliste[zahl] * 2)
    zahlenliste2.append(zahlenliste[zahl] * 2)

print('Vorher')
print(zahlenliste)

print('Nachher')
print(zahlenliste2)

zahlenliste.pop(3)
print('Nach dem löschen')
print(zahlenliste)



'''
Aufgabe2:
Gegeben ist folgende Liste: [15, 2, 39, 72, 142]
Schreibe eine App die eine neue Liste 
'''


