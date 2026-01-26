'''
Aufgabe1:
Gegeben ist folgende Liste: [15, 2, 39, 72, 142]
Schreibe eine App die jede Zahl in der Liste verdoppelt.
Benutze eine While-Schleife anstelle einer For-Schleife.
'''

zahlenliste = [15, 2, 39, 72, 142]
zähler = 0

while zähler < 5:
    zahlenliste[zähler] *= 2
    zähler += 1

print(zahlenliste)
