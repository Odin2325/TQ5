auswahl = input('Bitte geben Sie 1 für Pfannkuchen-Rezept, 2 für Waffeln-Rezept und 3 für Käsekuchen-Rezept: ')

try:
    auswahl = int(auswahl)
except:
    print('Bitte gib eine Zahl ein.')


if auswahl == 1:
    print('Pfannkuchen-Rezept: 200g Mehl, 200ml Milch, 2 Eier')
if auswahl == 2:
    print('Waffeln-Rezept: 300g Mehl, 300ml Milch, 3 Eier, 1 Packung Vanille-Zucker')
if auswahl == 3:
    print('Käsekuchen-Rezept: 400g Mehl, 400ml Milch, 4 Eier, 400g Quark, 1 Packung Vanille-Zucker')
