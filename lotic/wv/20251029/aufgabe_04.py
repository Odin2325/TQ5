# Aufgabe 4: Schleife über ein Dictionary
# Gegeben ist das Dictionary:
# inventar = {"apfel": 10, "banane": 5, "orange": 8}

# 1. Schreibe eine Schleife, die jede Frucht und die Anzahl ausgibt. Z.B.:

# for frucht in inventar: # alle Schlüssel werden durchlaufen
#    ... # Zugriff auf die Anzahl mittels inventar[frucht]

# oder mit inventar.items(), d.h alle (Schlüssel, Wert) - Paare werden durchlaufen

# for frucht, menge in inventar.items():
#    ...

# 2. Berechne die Gesamtanzahl aller Früchte.

inventar = {"apfel": 10, "banane": 5, "orange": 8}

for key in list(inventar.keys()):
  print(f'Frucht: {key} - Anzahl: {inventar[key]}')

print(f'Summe alle Früchte: {sum(list(inventar.values()))}')
