print('Ein Toller Addidtionsrechner')
print('Gib zwei zahlen ein.')

zahl1 = 0
zahl2 = 0
eingabe_gueltig = False

while not eingabe_gueltig:
    try:
        zahl1 = int(input('Erste Zahl: '))
        zahl2 = int(input('Zweite Zahl: '))
        eingabe_gueltig = True 
    except:
        print('Ungültige Eingabe')

if eingabe_gueltig:
    ergebnis = zahl1 + zahl2
    print(f'{zahl1} + {zahl2} = {ergebnis}')
