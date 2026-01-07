number = 1234321

n_string = str(number)
palindrom = True

for i in range(0, len(n_string)):
    if n_string[i] != n_string[len(n_string)-(i+1)]:
        palindrom = False

print(palindrom)
