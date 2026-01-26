# Summe einer Liste

# Aufgabe: Lies eine durch Leerzeichen getrennte Zahlenreihe vom Nutzer ein, speichere sie in einer Liste und gib die Summe aus.
# Beispiel: Input: "1 2 3 4" → Output: 10
'''
eingabe = input('Bitte geben Sie 4 Zahlen ein: ')

zahlen = list(map(int, eingabe.split()))

summe = sum(zahlen)

print('Die Summe ist:', summe)
'''

eingabe = input('Zahlen eingeben (durch leerzeichen getrennt): ')
zahlen = []

for wert in eingabe.split():
    if len(zahlen) == 4:
        print('Es wurden bereits 4 Zahlen eingegeben. Weitere werden ignoriert.')
        break
    try:
        zahlen.append(int(wert))
    except ValueError:
        print(f"'{wert}' ist keine Zahl und wird ignoriert.")
print('Die Summe ist:', sum(zahlen))