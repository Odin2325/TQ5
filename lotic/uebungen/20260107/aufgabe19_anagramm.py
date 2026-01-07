def checkAnagramm(string1, string2):
    if len(string1) != len(string2):
        return False
    string1_dict = {}
    for element in string1.lower():
        if not string1_dict.get(element):
            string1_dict[element] = 1
            continue
        string1_dict[element] += 1
    string2_dict = {}
    for element in string2.lower():
        if not string2_dict.get(element):
            string2_dict[element] = 1
            continue
        string2_dict[element] += 1
    for element in string1_dict.items():
        if not string2_dict.get(element[0]) == element[1]:
            return False
    return True

anagramm = checkAnagramm('Geburt', 'Betrug')
print(anagramm)




