# Aufgabe 3: Werte ändern und hinzufügen
# Ändere das Alter der Person im Dictionary person.
# Füge einen neuen Schlüssel 'beruf' mit einem selbstgewählten Wert hinzu.

person = {
  'name': 'John Doe',
  'alter': 41,
  'stadt': 'Stuttgart',
}

# Ändere das Alter der Person im Dictionary person.

person['alter'] = 71
person['beruf'] = 'Rentner'

print(person)
