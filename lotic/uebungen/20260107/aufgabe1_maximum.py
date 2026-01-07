example_list = [9, 11, 3, 25, 100, 6]

biggest_ele = example_list[0]

for i in range(1, len(example_list)):
    if example_list[i] > biggest_ele:
        biggest_ele = example_list[i]

print(biggest_ele)
