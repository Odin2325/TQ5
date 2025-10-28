
# Definiert euch eine Liste von ganzen Zahlen (um die 5 Stück).
# Diese Liste soll durchlaufen werden.
# Wenn die Zahl kleiner als 5 ist, soll ausgegeben werden "Die Zahl ... ist klein".
# Wenn die Zahl kleiner als 10 ist, soll ausgegeben werden "Die Zahl ... ist mittelgroß".
# Wenn die Zahl größer als 10 ist, soll ausgegeben werden "Die Zahl ... ist groß".
# Zusatzaufgabe:
# Gebt am Schluss eine Zusammenfassung aus, wie viele kleine, mittelgroße und große Zahlen in der Liste waren.

zahlen = [1, 4, 9, 5, 10, 11]

klein = 0
mittel = 0
gross = 0

for zahl in range(100):
    # erster Ansatz. Problem mit z.B. Zahl 1. die ist klein und mittelgroß gleichzeitig. häää
    # if zahl < 5:
    #     print(f'Die Zahl {zahl} ist klein')
    # if zahl < 10:
    #     print(f'Die Zahl {zahl} ist mittelgroß')
    # if zahl >= 10:
    #     print(f'Die Zahl {zahl} ist groß')

    # Reparaturvorschlag von Sönke, mit expliziteren Bedingungen
    # if zahl < 5:
    #     print(f'Die Zahl {zahl} ist klein')
    # if zahl >= 5 and zahl < 10:
    #     print(f'Die Zahl {zahl} ist mittelgroß')
    # if zahl >= 10:
    #     print(f'Die Zahl {zahl} ist groß')
    
    # Reparatur mit if-elif-else
    if zahl < 5:
        klein = klein + 1
        print(f'Die Zahl {zahl} ist klein')
    elif zahl < 10:
        mittel = mittel + 1
        print(f'Die Zahl {zahl} ist mittelgroß')
    else:
        gross = gross + 1
        print(f'Die Zahl {zahl} ist groß')

print('Zusammenfassung')
print(f'Es gab {klein} kleine Zahlen')
print(f'Es gab {mittel} mittelgroße Zahlen')
print(f'Es gab {gross} große Zahlen')
