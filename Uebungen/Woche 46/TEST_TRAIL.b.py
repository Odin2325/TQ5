print('Hallo Trail, Wie gehts Dir heute?') # Das ist ein beispielsatz für ein String.


name1 = 'Ionut'
name2 = 'Trail'
auto = 'Autohaus BMW'

print('Dieser Satz gehört ' + name1)
print('Heute kaufen ' + name1 + (' ') + name2 + ' bei BMW!!!') # Nicht 100 % richtig f-String vergessen
print(f'Heute kaufen {name1} {name2} im {auto}') # Richtige schreibweise mit F-String
print(auto[9:]) # Slicing (Zerteilen nach Index) Übung mit funktion x.find
print(auto.upper()) # Funktionen für Strigs (upper, lower)(Groß- und Kleinbuchstagen)
print(auto.split()) # Wörter trennung mit kommazeichen

x = 100

print(x) # Int-Variable x
print('x') #  Durch hochkomma wird x zum string

y = 25.25 # Python kennt nur punkt bei (float = Zahl mit kommastelle), (also nummern ohne kommas schreiben)

print(x + y) # Das ist addition 2er Variablen
print(x * y) # Das ist multiplikation 2er Variablen
print