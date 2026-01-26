# Errate-die-Zahl (mit Schleifen und input)

# Aufgabe: Programm wählt zufällige Zahl 1–20 (nutze random). Nutzer rät per input, Schleife läuft bis korrekt, nach jeder Eingabe Rückmeldung "größer/kleiner/korrekt" und Zähler der Versuche.

import random

zahl = random.randint(1, 20)
versuche = 0

print('Ich habe mir eine Zahl zwischen 1 und 20 ausgedacht.')

while True:
    try:
        tipp = int(input('Dein Tipp: '))
        versuche += 1

        if tipp < zahl:
            print('Die gesuchte Zahl ist größer.')
        elif tipp > zahl:
            print('Die gesuchte Zahl ist kleiner.')
        else:
            print('Koffektur!')
            print('Anzahl der Versuche:', versuche)
        break
    except ValueError:
        print('Bitte gib eine gültige Zahl ein.')