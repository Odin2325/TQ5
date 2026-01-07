daten = [1, 2, 2, 3, 3, 3, 4]
amount_dict = {}

for element in daten:
    if not amount_dict.get(element):
        amount_dict[element] = 1
        continue
    amount_dict[element] += 1
    
print(amount_dict)
