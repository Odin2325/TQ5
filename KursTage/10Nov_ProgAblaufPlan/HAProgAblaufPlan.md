# Programmablaufplan

## Aufgabenbeschreibung:

Ein Programm soll von einem Benutzer mehrere Zahlen einlesen und anschließend

* die größte Zahl,

* die kleinste Zahl

* und den Durchschnitt
berechnen und ausgeben.

Zuerst wird eingegeben, wie viele Zahlen verarbeitet werden sollen. Dann werden die Zahlen nacheinander eingelesen und ausgewertet.

## Pseudocode:

```python
EINGABE anzahl
summe ← 0
i ← 1

EINGABE zahl
groesste ← zahl
kleinste ← zahl
summe ← summe + zahl
i ← i + 1

SOLANGE i <= anzahl WIEDERHOLE
    EINGABE zahl
    summe ← summe + zahl

    WENN zahl > groesste DANN
        groesste ← zahl
    ENDE WENN

    WENN zahl < kleinste DANN
        kleinste ← zahl
    ENDE WENN

    i ← i + 1
ENDE SOLANGE

durchschnitt ← summe / anzahl

AUSGABE "Größte Zahl: ", groesste
AUSGABE "Kleinste Zahl: ", kleinste
AUSGABE "Durchschnitt: ", durchschnitt
```