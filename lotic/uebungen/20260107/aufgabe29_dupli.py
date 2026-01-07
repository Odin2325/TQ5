example_list = [1, 7, 14, 14, 33, 76, 76]

count_dict = {}

for element in example_list:
    if not count_dict.get(element):
        count_dict[element] = 1
        continue
    count_dict[element] += 1

for element in count_dict.items():
    # Nur elemente die exakt zweimal vorkommen.
    # Wenn elemente die mehr als zweimal vorkommen auch
    # als Duplikate zählen muss die folgende Zeile geändert werden
    # auf if element[1] >= 2
    if element[1] == 2:
        print(f'{element[0]} ist ein duplikat' )
