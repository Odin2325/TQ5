example_list = [14, 102, 5, 18, 27, 155, 76]
biggest = 0
second = 0

for element in example_list:
    if element >= biggest:
        second = biggest
        biggest = element

print(second)
