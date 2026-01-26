# Lösungen

Aufgaben vom 22-01-2026

## Lösung für Aufgabe 3-aa

| i  | CPULoad[i] | max | max2  |
| :- | :--------: | :-: | :---: |
| 0  | 12         | 12  | 0     |
| 1  | 10         | 10  | 0     |
| 2  | 40         | 40  | 10    |
| 3  | 73         | 73  | 40    |
| 4  | 33         | 73  | 40    |
| 5  | 60         | 60  | 40    |

## Lösung für Aufgabe 3-ab

Die Fehlerursache liegt in Zeile 17.
Hier wird max ein CPULoadwert zugewiesen, der kleiner als das bisherige max aber größer als max2 ist.

## Lösung für Aufgabe 3-ac

Ändere Zeile 17 in:

> `max2 = CPULoad[i];`


## Lösung für Aufgabe 3-ba

Vorzeichenbehaftete 32-Bit Integer erlauben Zahlen 

> **-2147483648 - 2147483647**

## Lösung für Aufgabe 3-bb

In max und max2 werden Prozentwerte gespeichert. Der Wertebereich liegt daher
zwischen 0 und 100.

> 100 >= max >= 0
>
> 100 >= max2 >= 0
>
> 255 >= Byte-Datentyp >= 0

Der Byte Datentyp kann zahlen von 0-255 speichern. Er ist also ausreichend und braucht bloß 8-Bit Speicher. Anstatt der 32-Bit die ein Integer benötigt.
