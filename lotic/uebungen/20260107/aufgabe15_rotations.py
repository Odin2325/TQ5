example_list = [1, 2, 3, 4]

example_list.insert(0, example_list[len(example_list)-1])
example_list.pop(len(example_list)-1)

print(example_list)
