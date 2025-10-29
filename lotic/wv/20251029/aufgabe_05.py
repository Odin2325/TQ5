# Aufgabe 5: Dictionary verschachteln
# Erstelle ein Dictionary schule mit zwei Schülern. Jeder Schüler soll ein weiteres Dictionary sein, das alter und noten enthält.
# Beispiel:
# schule = {
#    "Max": {"alter": 15, "noten": [1, 2, 3]},
#    "Anna": {"alter": 14, "noten": [2, 1, 2]}
# }

#1. Gib das Alter von Max aus.
#2. Berechne den Durchschnitt der Noten von Anna.

schule = {
  "Max": {"alter": 15, "noten": [1, 2, 3]},
  "Anna": {"alter": 14, "noten": [2, 1, 2]}
}

print(f'Das Alter von Max ist: {schule['Max']['alter']}')
print(f'Der Notendurchschnitt von Anna ist: {round(sum(schule['Anna']['noten']) / len(schule['Anna']['noten']), 2)}')
