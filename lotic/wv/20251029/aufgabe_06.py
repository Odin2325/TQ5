# Aufgabe 6: Dictionary filtern
# Gegeben ist ein Dictionary:
# preise = {"apfel": 2, "banane": 1, "kirsche": 3, "orange": 2}
# Erstelle ein neues Dictionary, das nur die Früchte enthält, die 2 Euro kosten oder weniger.

preise = {"apfel": 2, "banane": 1, "kirsche": 3, "orange": 2}

# Meine Lösung
billigeFruechte = {}

for key, value in preise.items():
  if value <= 2:
    billigeFruechte[key] = value

print(billigeFruechte)

# Lösung mit AI Unterstützung (dict comprehension)

billigeFruechte2 = {key: value for key, value in preise.items() if value <=2}
print(billigeFruechte2)
