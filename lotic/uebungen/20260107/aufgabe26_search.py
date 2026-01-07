example_list = [1, 7, 9, 25, 134]

def search_list(search, search_list):
    for element in enumerate(search_list):
        if search == element[1]:
            return element[0]
    return -1

index = search_list(25, example_list)
print(index)
