example_string = 'schifffahrt'
count_dict = {}

for letter in example_string:
    if not count_dict.get(letter):
        count_dict[letter] = 1
        continue
    count_dict[letter] += 1

print(count_dict)
