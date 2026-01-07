test_string = 'Asien'
voc_list = ['a', 'e', 'i', 'o', 'u']

voc_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for element in test_string.lower():
    if voc_dict.get(element) is not None:
        voc_dict[element] += 1

print(voc_dict)
