example_list = [8, 24, 1235, 12, 3, 6, 777]
smalest_ele = example_list[0]

for i in range (1, len(example_list)):
    if example_list[i] < smalest_ele:
        smalest_ele = example_list[i]

print(smalest_ele)
