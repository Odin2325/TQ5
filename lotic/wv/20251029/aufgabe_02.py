# Aufgabe 2: Werte abrufen
# Gegeben ist das Dictionary:
# student = {"name": "Max", "noten": [1, 2, 3, 4], "klasse": "10A"}
# 1. Gib den Namen des Studenten aus.
# 2. Gib die Notenliste aus (komplett oder jedes Element einzeln)
# 3. Berechne die Durchschnittsnote aus der Notenliste.

student = {
  "name": "Max",
  "noten": [1, 2, 3, 4],
  "klasse": "10A"
}

# 1. Ausgabe Name
print(f'Name des Studenten: {student['name']}')

# 2. Ausgabe Notenliste
print(student['noten'])

# Funktion zum berechnen des Notendurchschnitts
def avgGrade(gradeList):
  return sum(gradeList) / len(gradeList)

# 3. Ausgabe Notendurchschnitt
print(f'Notendurchschnitt: {avgGrade(student['noten'])}')
