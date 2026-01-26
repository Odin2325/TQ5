# Maximum und Minimum
# Aufgabe: Lies mehrere Zahlen ein und gib das größte und kleinste Element zusammen aus.
# Beispiel: Input: "4 2 9 1" → Output: "Max=9, Min=1"

# Funktion zum zahlen einlesen.
def zahl_einlesen(maximum, label):
    gueltige_zahl = False
    while not gueltige_zahl:
        zahl = input(label)
        try:
            zahl = int(zahl)
            if zahl <= maximum or not maximum:
                gueltige_zahl = True
            else:
                print('Zahl zu groß.')
        except:
            print('Bitte gib eine gültige Zahl ein')
    return zahl


gueltige_anzahl = False
anzahl_zahlen = zahl_einlesen(10, 'Wieviel Zahlen möchtest du einlesen (maximum 10)? ')

print(anzahl_zahlen)

zahlen = []

for i in range(1, anzahl_zahlen + 1):
    zahl = zahl_einlesen(0, 'Bitte Zahl eingeben: ')
    zahlen.append(zahl)

print(zahlen)

kleinste_zahl = zahlen[0] # initialisierung mit erstem element der Liste
groesste_zahl = zahlen[0] # initialisierung mit erstem element der Liste

for element in zahlen:
    if element < kleinste_zahl:
        kleinste_zahl = element
    if element > groesste_zahl:
        groesste_zahl = element

print(f'Die kleinste Zahl in der Liste ist {kleinste_zahl}')
print(f'Die groesste Zahl in der Liste ist {groesste_zahl}')

